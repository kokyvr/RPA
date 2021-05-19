#Librerias Python
import traceback
import pyautogui
import os
from pywinauto.application import Application
import keyboard
from keyboard import press
import time
#Librerias Propias
from .datos_bono import datos_bono
from .iniciar_sesion import iniciar_sesion
from tools.webdriver_chrome import webdriver_chrome
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains


def importar_web_mensajes(driver,bono):
    print('-'*80)
    try:
        dir = 'G:\\Mi unidad\\Casos\\Mensajes\\'
        list = os.listdir(dir) # dir is your directory path
        number_files = len(list)    
        for i in range(number_files):
            var_archivo = 'G:\Mi unidad\Casos\Mensajes\df_mensaje_{}.csv'.format(i+1)
            #Subiendo csv a la plataforma
            driver.find_element_by_xpath(bono['btn_carga_masiva']).click()
            time.sleep(10)
            driver.find_element_by_xpath(bono['btn_adjuntar']).click()
            time.sleep(10)
            keyboard.write(var_archivo)
            time.sleep(5)
            press('enter')
            time.sleep(2)
            alert = driver.switch_to_alert()
            alert.accept()
            time.sleep(2)
            print(f"Mensaje {driver.find_element_by_xpath(bono['btn_adjuntar']).text}")
            time.sleep(10)
            driver.find_element_by_xpath(bono['vista_previa']).click()
            time.sleep(10)
            # driver.find_element_by_xpath(bono['subir_mensaje']).click()            
            time.sleep(100)
            driver.back()

   
    except Exception as e:
        print(f"Existe un error : {traceback.format_exc()}")
    
    print('-'*80)


