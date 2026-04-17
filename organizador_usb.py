# =====================================
# Nombre: organizador_usb.py
# Autor: Alvin Gil
# Fecha: 22/03/2026
# Descripción: organizador automático de USB
# =====================================

import os
import shutil
from datetime import datetime

# Ruta USB
ruta_usb = "E:/"

# Clasificación de extensiones
tipos = {
    "imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".ico"],
    "videos": [".mp4", ".avi", ".mkv", ".mov"],
    "documentos": [".pdf", ".docx", ".txt", ".doc", ".xlsx"],
    "musica": [".mp3", ".wav", ".flac"],
    "comprimidos": [".zip", ".rar"],
    "programas": [".exe", ".bat", ".msi"],
    "iso": [".iso"],
    "html": [".html"],
    "js": [".js"],
    "css": [".css"],
}

# Función para obtener categoría según extensión
def obtener_categoria(extension):
    for categoria, extensiones in tipos.items():
        if extension in extensiones:
            return categoria
    return "otros"

# Recorremos todos los archivos en la USB
for archivo in os.listdir(ruta_usb):
    ruta_completa = os.path.join(ruta_usb, archivo)

    if os.path.isfile(ruta_completa):
        nombre, extension = os.path.splitext(archivo)
        extension = extension.lower()

        # Categoría
        categoria = obtener_categoria(extension)

        # Año de modificación
        fecha = os.path.getmtime(ruta_completa)
        año = datetime.fromtimestamp(fecha).year

        # Tamaño del archivo
        tamaño = os.path.getsize(ruta_completa)
        subcarpeta = "grandes" if tamaño > 50 * 1024 * 1024 else "normales"

        # Ruta de destino
        destino = os.path.join(ruta_usb, categoria, str(año), subcarpeta)

        if not os.path.exists(destino):
            os.makedirs(destino)

        # Mover archivo
        shutil.move(ruta_completa, os.path.join(destino, archivo))
        print(f"Movido: {archivo} → {destino}")

print("✅ Organización completa")



		
	