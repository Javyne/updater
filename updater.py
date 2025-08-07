import ctypes
import os
import sys

import requests


def mostrar_error(mensaje):
    # Mostrar una ventana emergente de error en Windows
    ctypes.windll.user32.MessageBoxW(0, mensaje, "Error de descarga", 0x10)


if getattr(sys, "frozen", False):
    # Si está congelado (ejecutable .exe)
    base_path = os.path.dirname(sys.executable)
else:
    # Si está corriendo como script .py
    base_path = os.path.dirname(os.path.abspath(__file__))

# Carpeta de descargas dentro de esa misma ruta
output_folder = os.path.join(base_path, "Descargas")

# Lista de URLs a descargar
urls = [
    "https://palsave.uriel6.duckdns.org/Level.sav",
    "https://palsave.uriel6.duckdns.org/LevelMeta.sav",
]

# Crear carpeta si no existe
os.makedirs(output_folder, exist_ok=True)

# Descargar los archivos
for url in urls:
    try:
        filename = url.split("/")[-1]
        filepath = os.path.join(output_folder, filename)

        response = requests.get(url)
        response.raise_for_status()

        with open(filepath, "wb") as f:
            f.write(response.content)

    except Exception as e:
        mensaje = f"No se pudo descargar:\n{url}\n\nError:\n{str(e)}"
        print(mensaje)
        mostrar_error(mensaje)
