#Librerias Python
import os
from numpy import set_string_function
import pyautogui
import time
import shutil
from PIL import Image, ImageGrab
import pywinauto
import traceback
from datetime import date
from datetime import timedelta
from pathlib import Path
#Librerias Python - Pandas
import pandas as pd
#Libreria Python - Selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
#Librerias Propias
from .datos_bono import datos_bono
from .iniciar_sesion import iniciar_sesion
from .descargar_web_adjunto import descargar_web_adjunto
from tools.webdriver_chrome import webdriver_chrome
from tools.esperar_archivo import esperar_archivo

def descargar_adjunto_por_informe(tipo_bono,caso,inicio,fin):
    bono = datos_bono(tipo_bono)
    #Iniciando Sesión
    contador = 5
    while contador==5:
        driver = webdriver_chrome()
        print(f'Ingresando a la página del {tipo_bono}')
        contador = iniciar_sesion(driver,bono)
        print(f'Logeo exitoso del {tipo_bono}')

    #Definiendo variables
    #url_user= 'https://casos.bono600.gob.pe/intranet_/?c=Registro&a=Editar&i={}'.format(df['ID'][0])
    field_search = '//div[@id="tblDatos_filter"]/label/input'
    ruta_origen_caso = r'C:\Users\acastaneda\Downloads\descarga.pdf'
    bono['ruta_origen'] = r'C:\Users\acastaneda\Downloads\reporte.xlsx'
    bono['datos_reporte'] = '//div[@id="tblDatos_info"]'
    bono['div_espera'] = '//div[@id="divEspera"]'
    bono['ruta_destino'] = r'{}\reporte.xlsx'.format(bono['ruta_bono'])
    bono['nombre_archivo'] = caso+"_casos_"+bono['bono']+"_"+inicio+"-"+fin+".xlsx"
    bono['ruta_new_nombre'] = r'{ruta_bono}\{caso}\{archivo}'.format(
                                ruta_bono=bono['ruta_bono'],
                                caso=caso,
                                archivo=bono['nombre_archivo'],
                                )


    tipo_caso = Select(driver.find_element_by_id('cboCaso'))
    tipo_caso.select_by_visible_text(caso)
    time.sleep(5)
    driver.find_element_by_xpath(bono['field_start_date']).send_keys(inicio)
    driver.find_element_by_xpath(bono['field_end_date']).send_keys(fin)
    time.sleep(5)
    driver.find_element_by_xpath(bono['btn_actualizar']).click()
    WebDriverWait(driver,100).until(EC.invisibility_of_element_located((By.XPATH, bono['div_espera'])))
    time.sleep(10)
    print(f"Valor de la Plataforma: {driver.find_element_by_xpath(bono['datos_reporte']).text}")

    #Eliminado archivo reporte previo
    if os.path.isfile(bono['ruta_origen']):
        print('Archivo previo encontrado para eliminar')
        os.remove(bono['ruta_origen'])
        
    driver.find_element_by_xpath(bono['btn_exportar']).click()
    time.sleep(2)
    alert = driver.switch_to_alert()
    alert.accept() 
    time.sleep(30)
    print(f"-Archivo descargado del {tipo_bono}, tipo de casos:{caso}")
    
    esperar_archivo(bono['ruta_origen'])

    shutil.move(bono['ruta_origen'], bono['ruta_destino'])
    os.rename(bono['ruta_destino'],bono['ruta_new_nombre'])

    print(f"Archivo movido del {tipo_bono} tipo de casos:{caso}")

    #Lectura del Documento
    df = pd.read_excel(
        bono['ruta_new_nombre'],
        sheet_name = 'Sheet1',
        converters={
        'DNI': lambda x: str(x),
        },
        skiprows = 4,
        usecols = 'A:AL')

    contador = 0
    for i in range(len(df)):
        if str(df['CASO'][i]) == caso :
            var_date = str(df['FECHA DE REGISTO'][i])[:10]
            contador += 1
            print('Iniciando el con caso:{} del DNI:{}'.format(df['CASO'][i],df['DNI'][i]))
            try:
                ruta_new_nombre = r'{ruta_bono}\{caso}\{nro}_{fecha}_{dni}.pdf'.format(
                                ruta_bono=bono['ruta_bono'],
                                caso=caso,
                                nro = str(contador),
                                fecha=var_date,
                                dni=str(df['DNI'][i]),
                                )
                filepath_png = r'{ruta_bono}\{caso}\{nro}_{fecha}_{dni}.png'.format(
                                ruta_bono=bono['ruta_bono'],
                                caso=caso,
                                nro = str(contador),
                                fecha=var_date,
                                dni=str(df['DNI'][i]),
                                )

                #Seleccionar DNI específico
                driver.find_element_by_xpath(field_search).send_keys(str(df['DNI'][i]))
                time.sleep(5)
                #Editar Valor
                driver.find_element_by_xpath(bono['btn_editar']).click()
                time.sleep(5)
                #Descargando archivos
                try:
                    driver.find_element_by_id('btnDoc1').click()
                    time.sleep(10)
                    pywinauto.mouse.click(button='left', coords=(1255,339))
                    # pywinauto.mouse.click(button='right', coords=(1115,595))
                    # pyautogui.click(button='right',x=1159, y=551)
                    # time.sleep(5)
                    # pyautogui.press('down')
                    # # send_keys('{ENTER}')
                    # time.sleep(5)
                    # pyautogui.press('enter')
                    time.sleep(10)
                    pyautogui.press('enter')
                    time.sleep(5)
                    print('En proceso del caso:{} del DNI:{}'.format(df['CASO'][i],df['DNI'][i]))
                    shutil.move(ruta_origen_caso, ruta_new_nombre)
                    # os.rename(ruta_destino,ruta_new_nombre)
                    print('Terminando el con caso:{} del DNI:{}'.format(df['CASO'][i],df['DNI'][i]))

                except:
                    screenshot = ImageGrab.grab(bbox=None)
                    screenshot.save(filepath_png, 'PNG')
                    print(f'Error{traceback.format_exc()}')
            except:
                time.sleep(500)
                screenshot = ImageGrab.grab(bbox=None)
                screenshot.save(filepath_png, 'PNG')
                print(f'Error {traceback.format_exc()}')
            
            driver.back()
            time.sleep(10)
    #Cerrar Sesión
    driver.quit()