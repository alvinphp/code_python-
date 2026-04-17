import zipfile
import os

# Directorio que contiene los archivos ZIP
# carpeta_zip = 'C:/Users/alvin/OneDrive/Escritorio/zip'
carpeta_zip = input("ingrese la ruta de la carpeta zip")
# Directorio destino para la descompresión
# carpeta_destino = 'C:/Users/alvin/OneDrive/Escritorio/zip'
carpeta_destino = carpeta_zip

if not os.path.exists(carpeta_zip):
    print("ruta invalida")
    exit()
    
# Iterar sobre todos los archivos en la carpeta
for archivo in os.listdir(carpeta_zip):
    if archivo.endswith('.zip'):
        ruta_completa = os.path.join(carpeta_zip, archivo)
        
        # Abrir y extraer el archivo ZIP
        with zipfile.ZipFile(ruta_completa, 'r') as zip_ref:
            zip_ref.extractall(carpeta_destino)
            print(f'Descomprimido: {archivo}')
