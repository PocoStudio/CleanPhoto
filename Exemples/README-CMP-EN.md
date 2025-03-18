# CleanPhoto
[![fr](https://img.shields.io/badge/Permuter_vers_:-fr-blue.svg)](https://github.com/PocoStudio/CleanPhoto/blob/main/Exemples/README-CMP-FR.md) [![nl](https://img.shields.io/badge/Veranderen_naar_:-nl-orange.svg)](https://github.com/PocoStudio/CleanPhoto/blob/main/Exemples/README-CMP-NL.md) [![dl](https://img.shields.io/badge/CleanPhoto-Download-darkgreen.svg)](https://github.com/PocoStudio/CleanPhoto/releases) [![Website](https://img.shields.io/badge/Website-Open-darkblue.svg)](https://cleanphoto.capiomont.fr/)<br/>
EN :
Welcome to CleanPhoto Tool!

***1. Run the executable to choose your version :***

- https://github.com/PocoStudio/CleanPhoto/releases


***2. Prerequisites to execute in Python (old version 1.0.0):***

Download the source folder above.

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

