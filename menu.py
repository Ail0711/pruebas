import argparse
import hashlib
from datetime import datetime
import platform
import os
import subprocess
import login as mix

# Crear un objeto ArgumentParser
parser = argparse.ArgumentParser(description="Aqui para entrar con el argparse")

# Agregar argumentos de entrada
parser.add_argument('argum1', type=str, help="Tipo de lenguaje -Poweshell, Bash o Python")
parser.add_argument('--accion', type=str, choices=['menu', 'script'], default='def', help="Entrar a un menú o iniciar un script")

# Parsear los argumentos de entrada
args = parser.parse_args()

def so_verif():
    sistema = platform.system()
    if sistema == "Windows":
        print("Sistema operativo: Windows")
        return "Windows"
    elif sistema == "Linux":
        print("Sistema operativo: Linux")
        return "Linux"
    else:
        print(f"Sistema operativo no reconocido: {sistema}")
        return None

def conect():
    mix.main()

def main():
    so = platform.system() 
    if args.accion=="menu":
        if so == "Windows":
            if args.argum1=="1":
                print
            elif args.argum1=="2":
                print("No se puede ejecutar en este sistema operativo")
            elif args.argum1=="3":
                conect()
    elif so == "Linux":
            if args.argum1=='1':
                print("No se puede ejecutar en este sistema operativo")
            elif args.argum1=='2':
                print
            elif args.argum1=='3':
                conect()

if __name__=="__main__":
    main()