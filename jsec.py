import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
from scapy.all import sniff
import pandas as pd
import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import defaultdict
import datetime

# Configuration Matplotlib
plt.style.use("ggplot")

# Dictionnaire pour stocker les paquets capturés
packet_counts = defaultdict(int)
packet_data = []  # Liste pour stocker les paquets

# Liste des filtres disponibles
FILTRES = {
    "Tous": "",
    "TCP": "tcp",
    "HTTPS": "tcp port 443",
    "DNS": "port 53"
}

capture_active = False  # Variable de contrôle

def packet_callback(packet):
    """ Fonction de rappel appelée à chaque paquet capturé """
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        proto = packet["IP"].proto
        proto_name = {6: "TCP", 17: "UDP", 1: "ICMP"}.get(proto, f"Autre ({proto})")

        packet_counts[proto_name] += 1  # Mise à jour des statistiques

        # Récupération des ports si disponibles
        src_port = packet["TCP"].sport if packet.haslayer("TCP") else (packet["UDP"].sport if packet.haslayer("UDP") else None)
        dst_port = packet["TCP"].dport if packet.haslayer("TCP") else (packet["UDP"].dport if packet.haslayer("UDP") else None)

        # Stocker les paquets capturés pour exportation
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        packet_info = {
            "Timestamp": timestamp,
            "Source IP": src_ip,
            "Destination IP": dst_ip,
            "Protocol": proto_name,
            "Source Port": src_port,
            "Destination Port": dst_port
        }
        packet_data.append(packet_info)

        # Affichage des paquets dans l'interface
        text_output.insert(tk.END, f"{timestamp} - {proto_name}: {src_ip} → {dst_ip} | Ports: {src_port} → {dst_port}\n")
        text_output.yview(tk.END)

def start_capture():
    """ Lance la capture des paquets """
    global capture_active
    if not capture_active:
        capture_active = True
        filtre_selectionne = filtre_var.get()
        filtre_bpf = FILTRES[filtre_selectionne]
        
        text_output.insert(tk.END, f"\n🔍 Capture démarrée avec filtre : {filtre_selectionne}...\n")
        
        thread = threading.Thread(target=sniff, kwargs={"filter": filtre_bpf, "prn": packet_callback, "store": False})
        thread.daemon = True
        thread.start()

def stop_capture():
    """ Stoppe la capture des paquets """
    global capture_active
    capture_active = False
    text_output.insert(tk.END, "\n🛑 Capture arrêtée.\n")

# Exportation en CSV
def export_csv():
    """ Exporte les paquets capturés en CSV """
    if not packet_data:
        text_output.insert(tk.END, "\n❌ Aucune donnée à exporter.\n")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])
    if file_path:
        df = pd.DataFrame(packet_data)
        df.to_csv(file_path, index=False)
        text_output.insert(tk.END, f"\n✅ Données exportées en CSV : {file_path}\n")

# Exportation en JSON
def export_json():
    """ Exporte les paquets capturés en JSON """
    if not packet_data:
        text_output.insert(tk.END, "\n❌ Aucune donnée à exporter.\n")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Fichiers JSON", "*.json")])
    if file_path:
        with open(file_path, "w") as f:
            json.dump(packet_data, f, indent=4)
        text_output.insert(tk.END, f"\n✅ Données exportées en JSON : {file_path}\n")

# Mise à jour du graphique en temps réel
def update_graph(i):
    plt.clf()
    if packet_counts:
        labels = list(packet_counts.keys())
        values = list(packet_counts.values())
        plt.bar(labels, values, color=['blue', 'green', 'red', 'purple'])
        plt.xlabel("Protocoles Réseau")
        plt.ylabel("Nombre de Paquets")
        plt.title("Statistiques des Paquets Capturés")
        plt.xticks(rotation=45)

# Ouvrir une fenêtre pour le graphique
def open_graph():
    global graph_window
    graph_window = tk.Toplevel(root)
    graph_window.title("Statistiques des Paquets")

    fig = plt.figure(figsize=(5, 4))
    canvas = tk.Canvas(graph_window, width=500, height=400)
    canvas.pack()

    ani = FuncAnimation(fig, update_graph, interval=1000)
    plt.show()

# Création de l'interface Tkinter
root = tk.Tk()
root.title("Analyseur Réseau - Sniffer GUI avec Export")
root.geometry("700x550")

# Sélection du filtre
tk.Label(root, text="Sélectionner le type de trafic à capturer :", font=("Arial", 12)).pack(pady=5)
filtre_var = tk.StringVar()
filtre_var.set("Tous")
filtre_menu = ttk.Combobox(root, textvariable=filtre_var, values=list(FILTRES.keys()), state="readonly")
filtre_menu.pack(pady=5)

# Boutons de contrôle
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)
btn_start = tk.Button(frame_buttons, text="Démarrer", command=start_capture, bg="green", fg="white", width=12)
btn_start.grid(row=0, column=0, padx=5)
btn_stop = tk.Button(frame_buttons, text="Arrêter", command=stop_capture, bg="red", fg="white", width=12)
btn_stop.grid(row=0, column=1, padx=5)
btn_graph = tk.Button(frame_buttons, text="Statistiques", command=open_graph, bg="blue", fg="white", width=12)
btn_graph.grid(row=0, column=2, padx=5)

# Boutons d'exportation
frame_export = tk.Frame(root)
frame_export.pack(pady=10)
btn_export_csv = tk.Button(frame_export, text="Exporter en CSV", command=export_csv, bg="orange", fg="black", width=15)
btn_export_csv.grid(row=0, column=0, padx=5)
btn_export_json = tk.Button(frame_export, text="Exporter en JSON", command=export_json, bg="purple", fg="white", width=15)
btn_export_json.grid(row=0, column=1, padx=5)

# Zone de texte pour afficher les paquets capturés
text_output = scrolledtext.ScrolledText(root, width=85, height=15, font=("Courier", 10))
text_output.pack(pady=5)

# Lancer l'interface
root.mainloop()
