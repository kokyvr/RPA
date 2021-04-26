#Librerias Python
import os
import shutil
import time

def esperar_archivo(nombre_archivo):
    while not os.path.isfile(nombre_archivo):
            print('Espera - Esperando tiempo adicional para descarga del archivo')
            time.sleep(60)

    if os.path.isfile(nombre_archivo):
        print('Espera - Esperando tiempo adicional para descarga del archivo')
        peso_inicial = os.path.getsize(nombre_archivo)
        time.sleep(30)
        peso_final = os.path.getsize(nombre_archivo)
        while peso_inicial != peso_final:
            print('Espera - Esperando un poco más para la descarga del archivo')
            peso_inicial = os.path.getsize(nombre_archivo)
            time.sleep(30)
            peso_final = os.path.getsize(nombre_archivo)