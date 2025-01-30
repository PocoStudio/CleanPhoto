# CleanPhoto
[![en](https://img.shields.io/badge/Change_to_:-en-darkred.svg)](https://github.com/PocoStudio/CleanPhoto/blob/main/Exemples/README-CMP-EN.md) [![nl](https://img.shields.io/badge/Veranderen_naar_:-nl-orange.svg)](https://github.com/PocoStudio/CleanPhoto/blob/main/Exemples/README-CMP-NL.md) [![dl](https://img.shields.io/badge/CleanPhoto-Télécharger-darkgreen.svg)](https://github.com/PocoStudio/CleanPhoto/releases)<br/>
FR :
Bienvenue sur l'outil CleanPhoto Tool ! 

***1. Lancer l'exécutable pour choisir sa version :***

- https://github.com/PocoStudio/CleanPhoto/releases


***2. Prérequis pour exécuter en Python (ancienne version 1.0.0):***

Télécharger le dossier source ci-dessus.

Installer les bibliothèques nécessaires avec les commandes suivantes :
- pip install pillow
- pip install ttkbootstrap
- pip install hachoir

***3. Pour compiler le code en exécutable (ancienne version 1.0.0):***

Télécharger le dossier source ci-dessus.

Prérequis : 
-> pip install pyinstaller

Compilation : Lancez la commande suivante dans le terminal :

pyinstaller --onefile --noconsole --icon=logo.ico --add-data "logo.png;." --hidden-import pillow --hidden-import hachoir --version-file=version.txt cleanphoto.py

![exemple_image1](https://github.com/user-attachments/assets/ef832a2c-ccfb-4021-b3de-27c5112cc546)
