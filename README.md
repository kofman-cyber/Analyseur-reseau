# 🕵️ Analyseur Réseau - Sniffer GUI avec Détection de Menaces

![GitHub](https://img.shields.io/github/license/kofman-cyber/analyseur-reseau)
![GitHub repo size](https://img.shields.io/github/repo-size/kofman-cyber/analyseur-reseau)
![GitHub contributors](https://img.shields.io/github/contributors/kofman-cyber/analyseur-reseau)

## 📌 Description
Ce projet est un **outil d'analyse réseau avancé** avec une **interface graphique (GUI)**.  
Il permet de **capturer et analyser le trafic réseau**, avec des fonctionnalités de :  
✅ Capture de paquets en temps réel 🛰  
✅ Sélection des filtres (TCP, HTTPS, DNS) 🎯  
✅ Détection d’attaques DoS & Scans de ports 🚨  
✅ Statistiques et visualisation des données 📊  
✅ Exportation des résultats en **CSV & JSON** 📁  

---

## 🎯 **Fonctionnalités**
- 📡 **Capture en temps réel** du trafic réseau avec `scapy`
- 🎛 **Interface Graphique (GUI)** avec **Tkinter**
- 🔎 **Filtrage des paquets** (TCP, HTTPS, DNS)
- 🚨 **Détection des menaces** (Attaque DoS, Scan de ports)
- 📊 **Affichage des statistiques en temps réel** (`matplotlib`)
- 📁 **Exportation des résultats** en **CSV & JSON**
- 🛠 **Compatible** avec **Windows & Linux**

---

## 📦 **Installation**
### 1️⃣ Prérequis
🔹 **Python 3.8+** doit être installé. Vérifie avec :
```bash
python --version
```
🔹 Installe les dépendances nécessaires :
```bash
pip install scapy matplotlib pandas
```
🔹 **Sur Windows**, installe **Npcap** (nécessaire pour `scapy`) :  
👉 [Télécharger Npcap](https://nmap.org/npcap/)

---

## 🚀 **Utilisation**
### 📌 Lancer l'outil
Exécute le script en **mode administrateur** :
```bash
python analyseur_reseau.py
```

### 📌 Interface Graphique (GUI)
1. **Choisir le type de trafic** à capturer (TCP, HTTPS, DNS).
2. **Cliquer sur "Démarrer"** pour lancer la capture.
3. **Les paquets s'affichent en temps réel**.
4. **Visualiser les statistiques** en cliquant sur **"Statistiques"**.
5. **Exporter les données** en CSV ou JSON.

---

## 🛡 **Détection des Menaces**
🔍 **Détection des Scans de Ports**  
➡️ Si une **IP tente +5 ports en <3 secondes**, une **alerte s'affiche**.  

🚨 **Détection des Attaques DoS**  
➡️ Si une **IP envoie +50 paquets en <3 secondes**, un **message d'alerte** apparaît.  

---

## 🖥 **Captures d'écran**
📌 **Interface principale**  
![Interface principale](https://via.placeholder.com/700x400?text=Capture+Interface)

📌 **Statistiques en temps réel**  
![Statistiques](https://via.placeholder.com/700x400?text=Graphiques+en+temps+r%C3%A9el)

📌 **Alertes de sécurité**  
![Alertes](https://via.placeholder.com/700x400?text=Detection+des+menaces)

---

## 🏗 **Améliorations futures**
✅ **Ajout d'une base de données pour stocker les menaces détectées**  
✅ **Intégration d'un moteur IA pour prédire les attaques**  
✅ **Envoi des alertes par e-mail ou webhook**  

---

## 🧑‍💻 **Contribuer**
Tu veux améliorer cet outil ? Voici comment contribuer :  
1. **Fork le projet** 📌  
2. **Crée une branche** (`git checkout -b feature-ma-nouvelle-fonction`)  
3. **Fais tes modifications** et **commit** (`git commit -m "Ajout de la nouvelle fonctionnalité"`)  
4. **Push ta branche** (`git push origin feature-ma-nouvelle-fonction`)  
5. **Crée une Pull Request** ✅  

---

## 📜 **Licence**
Ce projet est sous licence **MIT** 📝. Tu peux l'utiliser librement, mais merci de citer l'auteur.

---

## 💬 **Contact**
Si tu as des questions ou des suggestions, n'hésite pas à me contacter :  
📧 **Email** : `kouamekofman@gmail.com`    
📌 **GitHub** : https://github.com/kofman-cyber

---

### 🎯 **⭐ N'oublie pas de laisser une étoile sur le dépôt si ce projet te plaît !** ⭐  
```

---

## **📌 Explication des Sections**
🔹 **Description** → Présente ton outil et ses fonctionnalités principales.  
🔹 **Installation** → Explique comment installer les dépendances et exécuter le projet.  
🔹 **Utilisation** → Détaille les options de l'interface graphique.  
🔹 **Détection des menaces** → Montre comment ton outil repère les attaques DoS et scans.  
🔹 **Captures d’écran** → Permet aux utilisateurs de visualiser l’interface.  
🔹 **Améliorations futures** → Montre l’évolution prévue du projet.  
🔹 **Contribuer** → Guide les développeurs pour améliorer le projet.  
🔹 **Licence & Contact** → Fournit des informations légales et de contact.  

---

## **🚀 Prochaines Étapes**
✅ **Ajoute le fichier `README.md` à ton projet**  
✅ **Fais un commit et push sur GitHub** :
```bash
git add README.md
git commit -m "Ajout du fichier README.md"
git push origin main
```
✅ **Ajoute des captures d’écran** (remplace les liens `https://via.placeholder.com/...`).  
✅ **Personnalise ton contact & ton GitHub**.
