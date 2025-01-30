# CleanPhoto
EN :
Welcome to CleanPhoto Tool!

***1. Run the executable to choose your version :***

- https://github.com/PocoStudio/CleanPhoto/releases


***2. Prerequisites to execute in Python (old version 1.0.0):***

Download the source file above.

Install the necessary libraries with the following commands :
- pip install pillow
- pip install ttkbootstrap
- pip install hachoir

***3. To compile the code in an executable (old version 1.0.0):***

Download the source folder above.

Required libraries : 
-> pip install pyinstaller

Compilation : Launch following command in the terminal :

pyinstaller --onefile --noconsole --icon=logo.ico --add-data "logo.png;." --hidden-import pillow --hidden-import hachoir --version-file=version.txt cleanphoto.py
<br />
<br />
![exemple_image1](https://github.com/user-attachments/assets/ef832a2c-ccfb-4021-b3de-27c5112cc546)
<br />
<br />
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

