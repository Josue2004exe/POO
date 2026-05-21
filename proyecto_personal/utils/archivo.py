import os

def guardar_en_txt(ruta_archivo, datos):
    # 1. Crea las carpetas necesarias si no existen en tu computadora
    # os.makedirs: Extrae la ruta de la carpeta y la crea automáticamente si no existe en el disco duro; 
    # si ya existe, no hace nada (exist_ok=True).
    os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
    
    with open(ruta_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(datos + "\n")

def leer_txt(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        return []

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        return archivo.readlines()