# Programa para obtener password guardado en el windows.
# =====================================
# Nombre: wifi.py
# Autor: Alvin  Gil
# Fecha: 26/03/2026
# Descripción: obtener password guardados
# =====================================

import subprocess

def obtener_perfiles_wifi():
    comando = "netsh wlan show profiles"
    resultado = subprocess.check_output(comando, shell=True).decode('utf-8', errors="ignore")
    
    perfiles = []
    for linea in resultado.split('\n'):
        if "Perfil de todos los usuarios" in linea or "All User Profile" in linea:
            nombre = linea.split(":")[1].strip()
            perfiles.append(nombre)
    
    return perfiles

def obtener_password(perfil):
    try:
        comando = f'netsh wlan show profile name="{perfil}" key=clear'
        resultado = subprocess.check_output(comando, shell=True).decode('utf-8', errors="ignore")
        
        for linea in resultado.split('\n'):
            if "Contenido de la clave" in linea or "Key Content" in linea:
                return linea.split(":")[1].strip()
    except:
        return None

def main():
    perfiles = obtener_perfiles_wifi()
    
    print("\nRedes WiFi guardadas y sus contraseñas:\n")
    
    for perfil in perfiles:
        password = obtener_password(perfil)
        print(f"SSID: {perfil}")
        print(f"Password: {password}\n")

if __name__ == "__main__":
    main()