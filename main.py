import argparse
import hashlib
import os
import platform
from datetime import datetime

# Crear un objeto ArgumentParser
parser = argparse.ArgumentParser(description="Aqui para entrar con el argparse")

# Agregar argumentos de entrada
parser.add_argument('argumento1', type=int, help="Primer argumento")
parser.add_argument('argumento2', type=int, help="Segundo argumento")
parser.add_argument('--accion', type=str, choices=['non', 'non'], default='def', help="Operación a realizar")

# Parsear los argumentos de entrada
args = parser.parse_args()

def os_verif():
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
    
def generar_hash_archivo(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

    nombre_archivo = f"reporte.txt" #aqui ponemos el nombre del script 
    print(f"Tarea ejecutada: nombre del sript")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Hash del reporte: {hash_resultado}")
    print(f"Ubicación del archivo: {os.path.abspath(nombre_archivo)}")
