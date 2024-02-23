# Intranet Avancée

J'ai créer cette app Python pour mes besoins perso et elle marche parfaitement bien ! L'interface n'est pas moderne mais le principal c'est le fonctionnement, je vous autorise à modifier cette intranet et en faire des versions plus modernes ou avec des fonctions en plus.

## Installation Python et Modules Requis

1. **Installation de Python**: 🐍
   - Si vous n'avez pas Python installé sur votre système, téléchargez et installez la dernière version depuis le [site officiel de Python](https://www.python.org/downloads/).

2. **Modules Requis**: 🧩
   - Assurez-vous d'avoir les modules suivants installés :
     - `tkinter`: Ce module est inclus dans les installations Python par défaut.
     - `requests`: Pour effectuer des requêtes HTTP.
     - `json`: Pour la manipulation de fichiers JSON.
     - `webbrowser`: Pour ouvrir des liens web.
     - `Pillow`: Pour la manipulation d'images.

   Vous pouvez installer ces modules via pip (le gestionnaire de packages de Python) en exécutant les commandes suivantes dans votre terminal.


## Configuration du Mot de Passe et des Raccourcis d'Images ⚙️

### Changement du Mot de Passe Administrateur 🛠️
- Le mot de passe administrateur est défini dans la fonction `delete_shortcut()` du code.
- Vous pouvez le changer en modifiant la valeur de la variable `code`.
- Par défaut, le mot de passe est défini comme `"motdepassepardefaut"` à la `ligne 87`.

### Modification des Raccourcis d'Images 🖼️
- Les images sont chargées à partir d'un répertoire spécifique dans la fonction `update_image()` du code.
- Vous pouvez modifier le chemin du répertoire où se trouvent les images en changeant la valeur de la variable `directory` à la `ligne 138` et à la `ligne 142`.
- Assurez-vous que les images sont au format PNG et placez-les dans le répertoire spécifié.

## Utilisation 💻
- Après avoir installé Python et les modules requis, exécutez le script Python `intranet.py`.
- L'application s'ouvrira avec une interface graphique.
- Vous verrez des informations telles que l'heure actuelle, un message de bienvenue, des raccourcis personnalisés, et une image aléatoire.
- Vous pouvez ajouter des raccourcis personnalisés, changer le nom d'utilisateur et voir le message de salutation qui varie selon l'heure de la journée.
- Pour supprimer un raccourci, vous devez entrer le mot de passe administrateur.
- Vous pouvez également modifier le mot de passe administrateur en modifiant le code source du programme.
- Pour quitter l'application, fermez simplement la fenêtre principale.

Cette intranet ne sera pas maintenue à jour et il est même déconceiller de l'utiliser dans de grosses entreprises car celui-ci n'est pas le plus sécurisé, mais pour faire un mini intranet sur votre PC en local c'est ce qu'il vous faut ! 😌
