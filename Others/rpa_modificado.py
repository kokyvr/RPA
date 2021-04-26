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



def Bono_BFU(inicio,fin):
    CURR_DIR = os.getcwd()
    user = '07266464'
    pwd = 'L@urdes2013'
    ruta_origen = r'C:\Users\acastaneda\Downloads\reporte.xlsx'
    ruta_destino = r'G:\Mi unidad\Casos\Casos_BFU\reporte.xlsx'
    nombre_archivo = "casos_BFU_"+inicio+"-"+fin+".xlsx"
    ruta_new_nombre = Path("G:\Mi unidad\Casos\Casos_BFU",nombre_archivo)

    #URL
    url = 'https://casos.bfu.gob.pe/intranet_/index.php'
    #XPATH
    path_user = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[1]/input'
    path_pwd = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[2]/input'
    btn_enter = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[3]/input'
    btn_actualizar = '/html/body/div/div/div[1]/section[2]/div[1]/form/div[8]/button'
    field_start_date = '/html/body/div/div/div[1]/section[2]/div[1]/form/div[5]/input'
    field_end_date = '/html/body/div/div/div[1]/section[2]/div[1]/form/div[7]/input'
    btn_exportar = '/html/body/div/div/div[1]/section[2]/div[1]/form/div[9]/button'
    WebDriverChrome(url,path_user,user,path_pwd,pwd,btn_enter,field_start_date,inicio,field_end_date,fin,btn_actualizar,btn_exportar,ruta_origen,ruta_new_nombre,ruta_destino)

def Bono_RURAL(inicio,fin):
    CURR_DIR = os.getcwd()
    user = '07266464'
    pwd = 'L@urdes2013'
    ruta_origen = r'C:\Users\acastaneda\Downloads\reporte.xlsx'
    ruta_destino = r'G:\Mi unidad\Casos\Casos_RURAL\reporte.xlsx'
    nombre_archivo = "casos_RURAL_"+inicio+"-"+fin+".xlsx"
    ruta_new_nombre = Path("G:\Mi unidad\Casos\Casos_RURAL",nombre_archivo)

    #URL
    url = 'https://consultas.bonorural.pe/intranet_/index.php'
    #XPATH
    path_user = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[1]/input'
    path_pwd = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[2]/input'
    btn_enter = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[4]/input'
    btn_actualizar = '/html/body/div/div/div[1]/section[2]/div[1]/form/div[8]/button'
    field_start_date = '/html/body/div/div/div[1]/section[2]/div[1]/form/div[5]/input'
    field_end_date = '/html/body/div/div/div[1]/section[2]/div[1]/form/div[7]/input'
    btn_exportar = '/html/body/div/div/div[1]/section[2]/div[1]/form/div[9]/button'

    WebDriverChrome(url,path_user,user,path_pwd,pwd,btn_enter,field_start_date,inicio,field_end_date,fin,btn_actualizar,btn_exportar,ruta_origen,ruta_new_nombre,ruta_destino)


def Bono_600(inicio,fin):
    CURR_DIR = os.getcwd()
    user = '07266464'
    pwd = 'L@urdes2013'
    ruta_origen = r'C:\Users\acastaneda\Downloads\reporte.xlsx'
    ruta_destino = r'G:\Mi unidad\Casos\Casos_Bono600\reporte.xlsx'
    nombre_archivo = "casos_bono600_"+inicio+"-"+fin+".xlsx"
    ruta_new_nombre = Path("G:\Mi unidad\Casos\Casos_Bono600",nombre_archivo)

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
    WebDriverChrome(url,path_user,user,path_pwd,pwd,btn_enter,field_start_date,inicio,field_end_date,fin,btn_actualizar,btn_exportar,ruta_origen,ruta_new_nombre,ruta_destino)



def WebDriverChrome(url,path_user,user,path_pwd,pwd,btn_enter,field_start_date,inicio,field_end_date,fin,btn_actualizar,btn_exportar,ruta_origen,ruta_new_nombre,ruta_destino):
    #Abrir navegador
    #CURR_DIR = os.getcwd()
    ruta_chromedriver = 'G:\Mi unidad\RPA_bono600/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=ruta_chromedriver)
    #driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    
    #Acciones en la página
    driver.find_element_by_xpath(path_user).send_keys(user)
    driver.find_element_by_xpath(path_pwd).send_keys(pwd)
    time.sleep(15)
    driver.find_element_by_id('btnIngresar').click()
    time.sleep(15)

    """Exportar Información"""
    driver.find_element_by_xpath(field_start_date).send_keys(inicio)
    driver.find_element_by_xpath(field_end_date).send_keys(fin)
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

    driver.quit()

    shutil.move(ruta_origen, ruta_destino)
    os.rename(ruta_destino,ruta_new_nombre)


if __name__ == ('__main__'):
    date = date.today() - timedelta(days=1)
    inicio = '26032021'
    fin = date.strftime('%d%m%Y')
    #Bono_BFU(inicio,fin)
    #Bono_RURAL(inicio,fin)
    Bono_600(inicio,fin)
