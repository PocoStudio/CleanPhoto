# CleanPhoto
[![en](https://img.shields.io/badge/Change_to_:-en-darkred.svg)](https://github.com/PocoStudio/CleanPhoto/blob/main/Exemples/README-CMP-EN.md) [![fr](https://img.shields.io/badge/Permuter_vers_:-fr-blue.svg)](https://github.com/PocoStudio/CleanPhoto/blob/main/Exemples/README-CMP-FR.md) [![dl](https://img.shields.io/badge/CleanPhoto-Downloaden-darkgreen.svg)](https://github.com/PocoStudio/CleanPhoto/releases) [![Website](https://img.shields.io/badge/Website-Open-darkblue.svg)](https://cleanphoto.capiomont.fr/)<br/>
NL :
Welkom op CleanPhoto Tool ! 

***1. Voer het uitvoerbare bestand uit om de versie te selecteren :***

- https://github.com/PocoStudio/CleanPhoto/releases


***2. Vereisten voor het uitvoeren met Python (oude versie 1.0.0):***

Download het bovenstaande bronbestand.

Installeer de benodigde bibliotheken met de volgende commando's:
- pip install pillow
- pip install ttkbootstrap
- pip install hachoir

***3. Om de code te compileren tot een uitvoerbaar bestand (oude versie 1.0.0):***

Download het bovenstaande bronbestand.

Vereisten : 
-> pip install pyinstaller

Compilatie: Voer het volgende commando uit in de terminal:

pyinstaller --onefile --noconsole --icon=logo.ico --add-data "logo.png;." --hidden-import pillow --hidden-import hachoir --version-file=version.txt cleanphoto.py

![exemple_image1](https://github.com/user-attachments/assets/ef832a2c-ccfb-4021-b3de-27c5112cc546)
