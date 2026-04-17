import os
import re

ruta = "C:/Users/alvin/Downloads"

if not os.path.exists(ruta):
    print("❌ Ruta no encontrada")
    exit()

# Regex mejorado
patron = re.compile(r"\(\s*\d+\s*\)")

archivos = [f for f in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, f))]

for archivo in archivos:
    if patron.search(archivo):
        ruta_completa = os.path.join(ruta, archivo)
        try:
            os.remove(ruta_completa)
            print(f"🗑️ Eliminado: {archivo}")
        except Exception as e:
            print(f"⚠️ Error con {archivo}: {e}")

print("✅ Duplicados eliminados correctamente")