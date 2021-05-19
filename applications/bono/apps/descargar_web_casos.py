#Librerias Python
import os
import shutil
import time
#Libreria Python - Selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
#Librerias Propias
from tools.esperar_archivo import esperar_archivo

def descargar_web_casos(driver,bono,tipo_bono,caso):
    """Exportar Información"""
    if caso != 'todos' :
        tipo_caso = Select(driver.find_element_by_id('cboCaso'))
        tipo_caso.select_by_visible_text(caso)
        time.sleep(15)

    driver.find_element_by_xpath(bono['field_start_date']).send_keys(bono['valor_date'])
    driver.find_element_by_xpath(bono['field_end_date']).send_keys(bono['valor_date'])
    time.sleep(5)
    #wait = WebDriverWait(driver,10)
    #wait.until(ec.visibility_of_element_located((By.XPATH,btn_exportar)))
    driver.find_element_by_xpath(bono['btn_actualizar']).click()
    WebDriverWait(driver,100).until(EC.invisibility_of_element_located((By.XPATH, bono['div_espera'])))
    time.sleep(10)
    print(f"Fecha:{bono['valor_date']}-Valor de la Plataforma: {driver.find_element_by_xpath(bono['datos_reporte']).text}")

    #Eliminado archivo reporte previo
    if os.path.isfile(bono['ruta_origen']):
        print('Archivo previo encontrado para eliminar')
        os.remove(bono['ruta_origen'])
        
    driver.find_element_by_xpath(bono['btn_exportar']).click()
    time.sleep(2)
    alert = driver.switch_to_alert()
    alert.accept() 
    time.sleep(30)
    print(f"Fecha:{bono['valor_date']}-Archivo descargado del {tipo_bono}, tipo de casos:{caso}")
    
    esperar_archivo(bono['ruta_origen'])

    shutil.move(bono['ruta_origen'], bono['ruta_destino'])
    os.rename(bono['ruta_destino'],bono['ruta_new_nombre'])

    print(f"Fecha:{bono['valor_date']}-Archivo movido del {tipo_bono} tipo de casos:{caso}")