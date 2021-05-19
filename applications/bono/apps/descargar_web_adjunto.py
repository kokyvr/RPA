#Librerias Python
import os
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
from selenium.webdriver.common.by import By
#Librerias Propias
from .datos_bono import datos_bono

def descargar_web_adjunto(driver,bono):
    #Lectura del Documento
    df = pd.read_excel(
        r'{ruta_bono}\{caso}_casos_{tipo_bono}_{inicio}-{fin}.xlsx'.format(
            ruta_bono=bono['ruta_bono'],
            tipo_bono=bono['bono'],
            caso='todos',
            inicio=bono['valor_date'],
            fin=bono['valor_date'],
            ),
        sheet_name = 'Sheet1',
        converters={
        'DNI': lambda x: str(x),
        },
        skiprows = 4,
        usecols = 'A:AL')

    #Definiendo variables
    #url_user= 'https://casos.bono600.gob.pe/intranet_/?c=Registro&a=Editar&i={}'.format(df['ID'][0])
    field_search = '//div[@id="tblDatos_filter"]/label/input'
    div_espera = '//div[@id="divEspera"]'
    ruta_origen = r'C:\Users\acastaneda\Downloads\descarga.pdf'
    lst_caso = ["Deseo renunciar o devolver el bono","Registre su denuncia por suplantación",]
    
    
    driver.find_element_by_xpath(bono['field_start_date']).send_keys(bono['valor_date'])
    driver.find_element_by_xpath(bono['field_end_date']).send_keys(bono['valor_date'])
    time.sleep(5)
    driver.find_element_by_xpath(bono['btn_actualizar']).click()
    WebDriverWait(driver,100).until(EC.invisibility_of_element_located((By.XPATH, bono['div_espera'])))
    time.sleep(10)

    for caso in lst_caso:
        contador = 0
        for i in range(len(df)):
            if str(df['CASO'][i]) == caso :
                contador += 1
                print('Iniciando el con caso:{} del DNI:{}'.format(df['CASO'][i],df['DNI'][i]))
                try:
                    ruta_new_nombre = r'{ruta_bono}\{caso}\{fecha}_{nro}_{dni}.pdf'.format(
                                    ruta_bono=bono['ruta_bono'],
                                    caso=caso,
                                    nro = str(contador),
                                    fecha=bono['valor_date'],
                                    dni=str(df['DNI'][i]),
                                    )
                    filepath_png = r'{ruta_bono}\{caso}\{fecha}_{nro}_{dni}.png'.format(
                                    ruta_bono=bono['ruta_bono'],
                                    caso=caso,
                                    nro = str(contador),
                                    fecha=bono['valor_date'],
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
                        time.sleep(5)
                        # pywinauto.mouse.click(button='left', coords=(1260,290))
                        pywinauto.mouse.click(button='right', coords=(1115,595))
                        # pyautogui.click(button='right',x=1159, y=551)
                        time.sleep(5)
                        pyautogui.press('down')
                        # send_keys('{ENTER}')
                        time.sleep(5)
                        pyautogui.press('enter')
                        time.sleep(5)
                        pyautogui.press('enter')
                        time.sleep(5)
                        print('En proceso del caso:{} del DNI:{}'.format(df['CASO'][i],df['DNI'][i]))
                        shutil.move(ruta_origen, ruta_new_nombre)
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