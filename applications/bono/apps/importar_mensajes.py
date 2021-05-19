#Librerias Python
import traceback
import pyautogui
from pywinauto.application import Application
import keyboard
from keyboard import press
import time
#Librerias Propias
from .datos_bono import datos_bono
from .iniciar_sesion import iniciar_sesion
from .importar_web_mensajes import importar_web_mensajes
from tools.webdriver_chrome import webdriver_chrome
from tools.oracle.obtener_csv_oracle import obtener_csv_oracle


def importar_mensajes(tipo_bono):
    print('-'*80)
    try:
        #Definición de Datos
        bono = datos_bono(tipo_bono)
        bono['datos_reporte'] = '//div[@id="tblDatos_info"]'
        bono['div_espera'] = '//div[@id="divEspera"]'
        bono['btn_carga_masiva'] = '//b[contains(text(),"CARGA MASIVA DE AVANCES")]'
        bono['btn_adjuntar'] = '//button[@id="btnAdjuntarArchivo"]'
        bono['file_mensaje'] = '//button[@id="btnAdjuntarArchivo"]/b[2]'
        bono['vista_previa'] = '//button[@id="btnVistaPrevia"]'
        bono['subir_mensaje'] = '//button[@id="btnSubir"]'
        #Descargando archivos
        obtener_csv_oracle(bono['sigla'])

        #Iniciando Sesión
        contador = 5
        while contador==5:
            driver = webdriver_chrome()
            print(f'Ingresando a la página del {tipo_bono}')
            contador = iniciar_sesion(driver,bono)
            print(f'Logeo exitoso del {tipo_bono}')

        #Realizando operación
        importar_web_mensajes(driver,bono)
        
        #Cerrar Sesión
        driver.quit()

    except Exception as e:
        print(f"Existe un error en el {tipo_bono}: {traceback.format_exc()}")
    
    print('-'*80)


