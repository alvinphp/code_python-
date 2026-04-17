# =====================================
# Nombre: organize.py
# Autor: Alvin  Gil
# Fecha: 22/03/2026
# Descripción: automatizar descargas y ordenarla en carpetas
# =====================================
import os
import shutil
import schedule
import time

# carpeta de descarga
# carpeta_descargas = os.path.expanduser("~/Downloads")
carpeta_descargas = r"C:\Users\Alvin\Downloads"

# diccionario de extensiones y carpetas
extensiones = {
    ".pdf": "PDF",
    ".docx": "Word",
    ".doc": "Word",
    ".xlsx": "Excel",
    ".jpg": "Imagenes",
    ".jpeg": "Imagenes",
    ".png": "Imagenes",
    ".gif": "Imagenes",
    ".bmp": "Imagenes",
    ".tiff": "Imagenes",
    ".tif": "Imagenes",
    ".webp": "Imagenes",
    ".heic": "Imagenes",
    ".ico": "Imagenes",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".mkv": "Videos",
    ".mp3": "Musica",
    ".wav": "Musica",
    ".flac": "Musica",
    ".zip": "Comprimidos",
    ".rar": "Comprimidos",
    ".7z": "Comprimidos",
    ".exe": "Programas",
    ".msi": "Programas",
    ".bat": "Programas",
    ".txt": "Archivos notepad",
    ".csv": "Archivos notepad",
    ".iso": "iso",
    ".html": "Web",
    ".css": "Web",
    ".js": "Web",
}

# funcion para usar en schedule
def organizar():
    # recorrer archivos
    for archivo in os.listdir(carpeta_descargas):
        ruta_archivo = os.path.join(carpeta_descargas, archivo)

        # verificar que sea archivo
        if os.path.isfile(ruta_archivo):
            nombre, extension = os.path.splitext(archivo)

            # convertir a minúscula
            extension = extension.lower()

            if extension in extensiones:
                carpeta_destino = os.path.join(carpeta_descargas, extensiones[extension])

                # crear carpeta si no existe
                os.makedirs(carpeta_destino, exist_ok=True)

                # mover archivo
                destino = os.path.join(carpeta_destino, archivo)

                if not os.path.exists(destino):
                    shutil.move(ruta_archivo, destino)
                    print(f"Movido: {archivo} → {carpeta_destino}")

# importar cada minuto
# schedule.every(1).minutes.do(organizar)

# print("Ejecutando organizador cada minuto...")

# while True:
#     schedule.run_pending()
#     time.sleep(1)
organizar()