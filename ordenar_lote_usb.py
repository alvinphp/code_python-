import os
import shutil

ruta = "E:/"

orden = {
    ".pdf": 1,
    ".docx": 2,
    ".doc": 3,
    ".txt": 4,
    ".xls": 5,
    ".xlsx": 6,
    ".csv": 7,
    ".jpg": 8,
    ".jpeg": 9,
    ".png": 10,
    ".gif": 11,
    ".bmp": 12,
    ".mp3": 13,
    ".wav": 14,
    ".mp4": 15,
    ".mkv": 16,
    ".zip": 17,
    ".rar": 18,
    ".7z": 19,
    ".exe": 20,
    ".bat": 21,
    ".py": 22,
    ".html": 23,
    ".css": 24,
    ".js": 25
}

# Crear carpeta para mover carpetas existentes
carpetas_destino = os.path.join(ruta, "Carpetas")
os.makedirs(carpetas_destino, exist_ok=True)

# Mover carpetas existentes (ignorar Carpertas)
for item in os.listdir(ruta):
    ruta_item = os.path.join(ruta, item)
    if os.path.isdir(ruta_item) and item != "Carpetas":
        shutil.move(ruta_item, os.path.join(carpetas_destino, item))

# Listar archivos en la raíz
archivos = [f for f in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, f))]

# Agrupar archivos por extensión según orden
archivos_por_grupo = {}
for archivo in archivos:
    ext = os.path.splitext(archivo)[1].lower()
    if ext in orden:
        grupo = orden[ext]
        archivos_por_grupo.setdefault(grupo, []).append(archivo)

# Renombrar archivos de cada grupo consecutivamente
for grupo in sorted(archivos_por_grupo.keys()):
    archivos_grupo = archivos_por_grupo[grupo]
    for i, archivo in enumerate(sorted(archivos_grupo), 1):
        nuevo_nombre = f"{grupo:02d}_{i:03d}_{archivo}"
        os.rename(os.path.join(ruta, archivo), os.path.join(ruta, nuevo_nombre))

print("✅ Archivos renombrados correctamente, PDFs y Word ya no se intercalan.")