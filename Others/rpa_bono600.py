#import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os, shutil
import smtplib
import win32com.client
from datetime import datetime
from datetime import date
from datetime import timedelta
from pathlib import Path



if __name__ == ('__main__'):
    CURR_DIR = os.getcwd()
    user = '07266464'
    pwd = 'L@urdes2013'
    date = date.today() - timedelta(days=1)
    yesterday = date.strftime('%d%m%Y')
    ruta_origen = r'C:\Users\acastaneda\Downloads\reporte.xlsx'
    ruta_destino = r'G:\Mi unidad\Casos\Casos_Bono600\reporte.xlsx'
    nombre_archivo = "casos_bono600_"+ yesterday+".xlsx"
    ruta_new_nombre = Path("G:\Mi unidad\Casos\Casos_Bono600",nombre_archivo)


    # message = 'Ingrese a la plataforma'
    # subject = 'Ingrese'
    # message = f'Subject: {message} \n\n {subject}'
    # server = smtplib.SMTP('smtp.gmail.com',587)
    # server.starttls()
    # server.login('contratista02@pension65.gob.pe', 'tribich.123')



    #URL
    url = 'https://casos.bono600.gob.pe/intranet_/index.php'
    #XPATH
    path_user = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[1]/input'
    path_pwd = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[2]/input'
    btn_enter = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[3]/input'
    btn_actualizar = '/html/body/div/div/div[2]/section[2]/div[1]/form/div[8]/button'
    field_start_date = '/html/body/div[1]/div/div[2]/section[2]/div[1]/form/div[5]/input'
    field_end_date = '/html/body/div[1]/div/div[2]/section[2]/div[1]/form/div[7]/input'
    btn_exportar = '/html/body/div[1]/div/div[2]/section[2]/div[1]/form/div[9]/button'

    #Abrir navegador
    #CURR_DIR = os.getcwd()
    ruta_chromedriver = 'G:\Mi unidad\RPA_bono600/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=ruta_chromedriver)
    #driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    #shell = win32com.client.Dispatch("WScript.Shell")

    #Acciones en la página
    driver.find_element_by_xpath(path_user).send_keys(user)
    driver.find_element_by_xpath(path_pwd).send_keys(pwd)
    time.sleep(10)
    driver.find_element_by_xpath(btn_enter).click()
    time.sleep(10)

    """Exportar Información"""
    driver.find_element_by_xpath(field_start_date).send_keys(yesterday)
    driver.find_element_by_xpath(field_end_date).send_keys(yesterday)
    time.sleep(15)
    #wait = WebDriverWait(driver,10)
    #wait.until(ec.visibility_of_element_located((By.XPATH,btn_exportar)))
    driver.find_element_by_xpath(btn_actualizar).click()
    time.sleep(30)
    driver.find_element_by_xpath(btn_exportar).click()
    time.sleep(2)
    alert = driver.switch_to_alert()
    alert.accept() 
    time.sleep(30)
    #server.sendmail('contratista02@pension65.gob.pe','alxcasta13@gmail.com',message)

    #server.quit()
    driver.quit()


    shutil.move(ruta_origen, ruta_destino)
    os.rename(ruta_destino,ruta_new_nombre)