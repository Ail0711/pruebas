import argparse
import hashlib
import os
import platform
import subprocess
from datetime import datetime
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

def main():
    so = so_verif
    print("Windochafa")
    
    if so=="Windows":
        print("Windo")
        if argparse.accion=='menu':
            if argparse.argum1=='powershell':
                print
            elif argparse.argum1=='bash':
                print
            elif argparse.argum1=='Pyhton':
                mix.main
    elif so == "Linux":
            if argparse.argum1=='bash':
                print
            elif argparse.argum1=='Pyhton':
                print
if __name__=="__main__":
    main()
