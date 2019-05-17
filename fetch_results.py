#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

with open("./store.txt","r+") as f:
    cont=str(f.read()).split(" , ")

with open("./pingresults.txt","w") as f:
    if(str(cont)!="['']"):
        f.write(str(cont))
        print(str(cont))
        print("\nDie Dateien wurden unter dem Namen \"pingresults.txt\" als JSON-Datei im Anwendungsverzeichnis gespeichert.")
    else:
        print("Die Ergebnissliste ist leer. Nutzen Sie zuerst ping-tool.py und versuchen es erneut.")
