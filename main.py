import argparse
import hashlib
import os
import platform
import subprocess
from datetime import datetime

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
    if argparse.accion=='menu':
        if so=="Windows":
            if argparse.argum1=='powershell':
                print
            elif argparse.argum1=='bash':
                print
            elif argparse.argum1=='Pyhton':
                print
        elif so == "Linux":
            if argparse.argum1=='bash':
                print
            elif argparse.argum1=='Pyhton':
                print
    elif argparse.accion=='script':

def generar_hash_archivo(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

#-------------------------------------------------------------------------------- para poweshell asi deberia de funcionar creo 
ruta_script = "C:\\ruta al script.ps1"

# Comando para ejecutar el script de PowerShell
try:
    resultado = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", ruta_script], 
                               capture_output=True, text=True, check=True)
    # Mostrar la salida en la terminal
    print("Salida del script:")
    print(resultado.stdout)
except subprocess.CalledProcessError as e:
    print("Error al ejecutar el script:")
    print(e.stderr)
#--------------------------------------------------------------------------------

    hash_resultado = generar_hash_archivo(nombre_archivo)
    nombre_archivo = f"reporte.txt" #aqui ponemos el nombre del script 
    print(f"Tarea ejecutada: nombre del sript")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Hash del reporte: {hash_resultado}")
    print(f"Ubicación del archivo: {os.path.abspath(nombre_archivo)}")
