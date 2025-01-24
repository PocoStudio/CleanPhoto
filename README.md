# CleanPhoto
Bienvenue sur l'outil CleanPhoto Tool ! 

***1. Prérequis pour exécuter en Python :***

Installer les bibliothèques nécessaires avec les commandes suivantes :
-> pip install pillow
-> pip install ttkbootstrap
-> pip install hachoir

***2. Pour compiler le code en exécutable :***

Prérequis : 
-> pip install pyinstaller

Compilation : Lancez la commande suivante dans le terminal :

pyinstaller --onefile --noconsole --icon=logo.ico --add-data "logo.png;." --hidden-import pillow --hidden-import hachoir --version-file=version.txt cleanphoto.py

