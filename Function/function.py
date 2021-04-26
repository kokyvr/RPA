#Python
import time
import os, shutil
import smtplib
import win32com.client
from datetime import datetime
from datetime import date
from datetime import timedelta
from pathlib import Path
import traceback
from PIL import ImageGrab
import pyautogui
from keyboard import press
#Pywinauto
import pywinauto
from pywinauto.keyboard import send_keys
#Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
#Pandas
import pandas as pd
#Oracle
import cx_Oracle
#Propias
from Tools import config
from Tools import tool_files


def Datos_Bono(bono):
    my_dict_bono = {}
    if bono == 'Bono BFU':
        #Insertar datos al dictionario my_dict_bono
        my_dict_bono['sigla'] = 'BFU'
        my_dict_bono['bono'] = 'Bono BFU'
        my_dict_bono['user'] = '07266464'
        my_dict_bono['pwd'] = 'L@urdes2013'
        my_dict_bono['ruta_bono'] = r'G:\Mi unidad\Casos\Casos_BFU'
        my_dict_bono['url'] = 'https://casos.bfu.gob.pe/intranet_/index.php'
        my_dict_bono['url_alternativo'] = 'https://casos.bfu.gob.pe/intranet_/'
        my_dict_bono['path_user'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[1]/input'
        my_dict_bono['path_pwd'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[2]/input'
        my_dict_bono['btn_enter'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[3]/input'
        my_dict_bono['btn_actualizar'] = '//button[@id="btnMostrar"]'
        my_dict_bono['field_start_date'] = '//input[@id="txtFechaConsulta"]'
        my_dict_bono['field_end_date'] = '//input[@id="txtFechaConsultaFin"]'
        my_dict_bono['btn_exportar'] = '//button[@id="btnExportarRegistrosFecha"]'
        
    elif bono == 'Bono RURAL':
        my_dict_bono['sigla'] = 'RURAL'
        my_dict_bono['bono'] = 'Bono RURAL'
        #Insertar datos al dictionario my_dict_bono
        my_dict_bono['user'] = '07266464'
        my_dict_bono['pwd'] = 'L@urdes2013'
        my_dict_bono['ruta_bono'] = r'G:\Mi unidad\Casos\Casos_RURAL'
        my_dict_bono['url'] = 'https://consultas.bonorural.pe/intranet_/'
        my_dict_bono['url_alternativo'] = 'https://consultas.bonorural.pe/intranet_/index.php'
        my_dict_bono['path_user'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[1]/input'
        my_dict_bono['path_pwd'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[2]/input'
        my_dict_bono['btn_enter'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[4]/input'
        my_dict_bono['btn_actualizar'] = '//button[@id="btnMostrar"]'
        my_dict_bono['field_start_date'] = '//input[@id="txtFechaConsulta"]'
        my_dict_bono['field_end_date'] = '//input[@id="txtFechaConsultaFin"]'
        my_dict_bono['btn_exportar'] = '//button[@id="btnExportarRegistrosFecha"]'

    elif bono == 'Bono URBANO':
        #Insertar datos al dictionario my_dict_bono
        my_dict_bono['sigla'] = 'URBANO'
        my_dict_bono['bono'] = 'Bono URBANO'
        my_dict_bono['user'] = '07266464'
        my_dict_bono['pwd'] = 'L@urdes2013'
        my_dict_bono['ruta_bono'] = r'G:\Mi unidad\Casos\Casos_URBANO'
        #URL
        my_dict_bono['url'] = 'https://consultas.yomequedoencasa.pe/intranet_/index.php?alter=5'
        my_dict_bono['url_alternativo'] = 'https://consultas.yomequedoencasa.pe/intranet_/'
        #XPATH
        my_dict_bono['path_user'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[1]/input'
        my_dict_bono['path_pwd'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[2]/input'
        my_dict_bono['btn_enter'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[4]/input'
        my_dict_bono['btn_actualizar'] = '//button[@id="btnMostrar"]'
        my_dict_bono['field_start_date'] = '//input[@id="txtFechaConsulta"]'
        my_dict_bono['field_end_date'] = '//input[@id="txtFechaConsultaFin"]'
        my_dict_bono['btn_exportar'] = '//button[@id="btnExportarRegistrosFecha"]'

    elif bono == 'Bono 600':
        #Insertar datos al dictionario my_dict_bono
        my_dict_bono['sigla'] = '600'
        my_dict_bono['bono'] = 'Bono 600'
        my_dict_bono['user'] = '07266464'
        my_dict_bono['pwd'] = 'L@urdes2013'
        my_dict_bono['ruta_bono'] = r'G:\Mi unidad\Casos\Casos_Bono600'
        #URL
        my_dict_bono['url'] = 'https://casos.bono600.gob.pe/intranet_/index.php'
        my_dict_bono['url_alternativo'] = 'https://casos.bono600.gob.pe/intranet_/'
        #XPATH
        my_dict_bono['path_user'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[1]/input'
        my_dict_bono['path_pwd']= '/html/body/div[1]/div/div/div/article/div/div/div/form/div[2]/input'
        my_dict_bono['btn_enter'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[3]/input'
        my_dict_bono['btn_actualizar'] = '//button[@id="btnMostrar"]'
        my_dict_bono['field_start_date'] = '//input[@id="txtFechaConsulta"]'
        my_dict_bono['field_end_date'] = '//input[@id="txtFechaConsultaFin"]'
        my_dict_bono['btn_exportar'] = '//button[@id="btnExportarRegistrosFecha"]'
    else:
        print('Error en la digitación')
    return my_dict_bono


def webdriver_chrome():
    #Webdriver
    ruta_chromedriver = 'C:\chromedriver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=ruta_chromedriver)

    return driver


def webdriver_chrome_exp():
    #Webdriver
    ruta_chromedriver = 'C:\chromedriver/chromedriver.exe'
    ####Opcion 01
    # options = webdriver.ChromeOptions()

    # # options.addArguments("--browser.helperApps.neverAsk.saveToDisk=application/pdf")
    # options.add_experimental_option('prefs', {
    # # "browser.helperApps.neverAsk.saveToDisk":"application/pdf",
    # # "download.default_directory": "C:/Users/XXXX/Desktop", #Change default directory for downloads
    # "download.prompt_for_download": False, #To auto download the file
    # # "download.directory_upgrade": True,
    # # "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
    # })
    # Opcion 02
    options = webdriver.ChromeOptions()
    # prefs = {'profile.default_content_setting_values.automatic_downloads': 1, 'profile.default_content_settings.popups': 0}
    prefs = {"plugins.always_open_pdf_externally": True}
    options.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(executable_path=ruta_chromedriver,options=options)

    return driver


def Iniciar_Sesion(driver,url,url_alternativo,pwd,path_pwd,user,path_user):
    try:
        #Variable Espera
        div_espera = '//div[@id="divEspera"]'
        inicio = True
        contador = 1
        while inicio == True:
            #Inicios alternativos
            if contador % 2 != 0:
                driver.maximize_window()
                driver.get(url)
            else:
                driver.maximize_window()
                driver.get(url_alternativo)
            
            contador +=1

            #Acciones en la página
            driver.find_element_by_xpath(path_user).send_keys(user)
            driver.find_element_by_xpath(path_pwd).send_keys(pwd)
            time.sleep(5)
            driver.find_element_by_id('btnIngresar').click()
            time.sleep(15)
            # WebDriverWait(driver,100).until(EC.invisibility_of_element_located((By.XPATH, div_espera)))
            print('Ingresando a la plataforma')
            try:
                driver.find_element_by_id('btnIngresar')
                print('Error en el ingreso, intentantando nuevamente')
                inicio = True
            except:
                print('Se accedio a la plataforma de forma satisfactoria')
                inicio = False
    except:
        print(traceback.format_exc())



def espera_archivo(nombre_archivo):
    while not os.path.isfile(nombre_archivo):
            print('Espera 01 - Esperando tiempo adicional para descarga del archivo')
            time.sleep(60)

    if os.path.isfile(nombre_archivo):
        print('Espera 02 - Archivo descargado esperando tiempo adicional para descarga del archivo')
        peso_inicial = os.path.getsize(nombre_archivo)
        time.sleep(30)
        peso_final = os.path.getsize(nombre_archivo)
        while peso_inicial != peso_final:
            print('Espera 03 - Archivo descargado esperando un poco más para la descarga del archivo')
            peso_inicial = os.path.getsize(nombre_archivo)
            time.sleep(30)
            peso_final = os.path.getsize(nombre_archivo)


def Descargar_Informe(tipo_bono,inicio,fin,caso = 'todos'):
    print('-'*80)
    try:
        #Definición de Datos
        bono = Datos_Bono(tipo_bono)
        ruta_del_bono = bono['ruta_bono']
        bono['ruta_origen'] = r'C:\Users\acastaneda\Downloads\reporte.xlsx'
        bono['ruta_destino'] = r'{}\reporte.xlsx'.format(ruta_del_bono)
        bono['nombre_archivo'] = caso+"_casos_"+bono['bono']+"_"+inicio+"-"+fin+".xlsx"
        bono['ruta_new_nombre'] = Path(bono['ruta_bono'],bono['nombre_archivo'])
        datos_reporte = '//div[@id="tblDatos_info"]'
        div_espera = '//div[@id="divEspera"]'


        #Iniciando Sesión
        driver = webdriver_chrome_exp()
        print(f'Fecha:{inicio}-Ingresando a la página del {tipo_bono}, tipo de casos:{caso}')
        Iniciar_Sesion(driver,bono['url'],bono['url_alternativo'],bono['pwd'],bono['path_pwd'],bono['user'],bono['path_user'])
        print(f'Fecha:{inicio}-Logeo exitoso del {tipo_bono}, tipo de casos:{caso} ')

        """Exportar Información"""
        if caso != 'todos' :
            tipo_caso = Select(driver.find_element_by_id('cboCaso'))
            tipo_caso.select_by_visible_text(caso)
            time.sleep(15)

        driver.find_element_by_xpath(bono['field_start_date']).send_keys(inicio)
        driver.find_element_by_xpath(bono['field_end_date']).send_keys(fin)
        time.sleep(5)
        #wait = WebDriverWait(driver,10)
        #wait.until(ec.visibility_of_element_located((By.XPATH,btn_exportar)))
        driver.find_element_by_xpath(bono['btn_actualizar']).click()
        WebDriverWait(driver,100).until(EC.invisibility_of_element_located((By.XPATH, div_espera)))
        time.sleep(10)
        print(f'Fecha:{inicio}-Valor de la Plataforma: {driver.find_element_by_xpath(datos_reporte).text}')
        
        #Eliminado archivo reporte previo
        if os.path.isfile(bono['ruta_origen']):
            print('Archivo previo encontrado para eliminar')
            os.remove(bono['ruta_origen'])
        
        driver.find_element_by_xpath(bono['btn_exportar']).click()
        time.sleep(2)
        alert = driver.switch_to_alert()
        alert.accept() 
        time.sleep(30)
        print(f'Fecha:{inicio}-Archivo descargado del {tipo_bono}, tipo de casos:{caso}')
        
        while not os.path.isfile(bono['ruta_origen']):
            print('Espera 01 - Esperando tiempo adicional para descarga del archivo')
            time.sleep(60)

        if os.path.isfile(bono['ruta_origen']):
            print('Espera 02 - Archivo descargado esperando tiempo adicional para descarga del archivo')
            peso_inicial = os.path.getsize(bono['ruta_origen'])
            time.sleep(30)
            peso_final = os.path.getsize(bono['ruta_origen'])
            while peso_inicial != peso_final:
                print('Espera 03 - Archivo descargado esperando un poco más para la descarga del archivo')
                peso_inicial = os.path.getsize(bono['ruta_origen'])
                time.sleep(30)
                peso_final = os.path.getsize(bono['ruta_origen'])

        shutil.move(bono['ruta_origen'], bono['ruta_destino'])
        os.rename(bono['ruta_destino'],bono['ruta_new_nombre'])
        print(f'Fecha:{inicio}-Archivo movido del {tipo_bono} tipo de casos:{caso}')
        driver.quit()
    except Exception as e:
        print(f'Fecha:{inicio}-Existe un error en el {tipo_bono}: {traceback.format_exc()}, tipo de casos:{caso}')
    
    print('-'*80)


def Descargar_pdf(tipo_bono,caso,inicio,fin):
    time.sleep(10)

    # pyautogui.FAILSAFE = False
    bono = Datos_Bono(tipo_bono)
    df = pd.read_excel(
        r'{ruta_bono}\{caso}_casos_{tipo_bono}_{inicio}-{fin}.xlsx'.format(
            ruta_bono=bono['ruta_bono'],
            tipo_bono=bono['bono'],
            caso='todos',
            inicio=inicio,
            fin=fin,
            ),
        sheet_name = 'Sheet1',
        skiprows = 4,
        usecols = 'A:AL')
    
    #url_user= 'https://casos.bono600.gob.pe/intranet_/?c=Registro&a=Editar&i={}'.format(df['ID'][0])
    field_search = '//div[@id="tblDatos_filter"]/label/input'
    btn_editar = '//button[@title="Editar"]'
    div_espera = '//div[@id="divEspera"]'
    ruta_origen = r'C:\Users\acastaneda\Downloads\descarga.pdf'
    ruta_destino = r'{ruta_bono}\{caso}\descarga.pdf'.format(
                                ruta_bono=bono['ruta_bono'],
                                caso=caso,
                                )

     
    #Iniciando Sesión
    driver = webdriver_chrome()
    print(f'Ingresando a la página del {tipo_bono}, tipo de casos:{caso}')
    Iniciar_Sesion(driver,bono['url'],bono['url_alternativo'],bono['pwd'],bono['path_pwd'],bono['user'],bono['path_user'])
    print(f'Logeo exitoso del {tipo_bono}, tipo de casos:{caso} ')
    # Ingresar al listado de casos 
    driver.find_element_by_xpath(bono['field_start_date']).send_keys(inicio)
    driver.find_element_by_xpath(bono['field_end_date']).send_keys(fin)
    time.sleep(5)
    driver.find_element_by_xpath(bono['btn_actualizar']).click()
    WebDriverWait(driver,100).until(EC.invisibility_of_element_located((By.XPATH, div_espera)))
    time.sleep(5)
    print('Número de elementos {}'.format(len(df)))
    for i in range(len(df)):
        if str(df['CASO'][i]) == caso :
            print('Iniciando el con caso:{} del DNI:{}'.format(df['CASO'][i],df['DNI'][i]))
            try:
                ruta_new_nombre = r'{ruta_bono}\{caso}\{nro}_{fecha}_{dni}.pdf'.format(
                                ruta_bono=bono['ruta_bono'],
                                caso=caso,
                                nro = str(df['Nro.'][i]),
                                fecha=inicio,
                                dni=str(df['DNI'][i]),
                                )
                filepath_png = r'{ruta_bono}\{caso}\{nro}_{fecha}_{dni}.png'.format(
                                ruta_bono=bono['ruta_bono'],
                                caso=caso,
                                nro = str(df['Nro.'][i]),
                                fecha=inicio,
                                dni=str(df['DNI'][i]),
                                )

                #Seleccionar DNI específico
                driver.find_element_by_xpath(field_search).send_keys(str(df['DNI'][i]))
                time.sleep(5)
                #Editar Valor
                driver.find_element_by_xpath(btn_editar).click()
                time.sleep(5)
                #Descargando archivos
                try:
                    driver.find_element_by_id('btnDoc1').click()
                    time.sleep(5)
                    #### Opcion 01
                    # pywinauto.mouse.click(button='left', coords=(931,761))
                    pywinauto.mouse.click(button='right', coords=(1159,551))
                    # pyautogui.click(button='right',x=1159, y=551)
                    time.sleep(5)
                    # send_keys('{DOWN}')
                    pyautogui.press('down')
                    time.sleep(5)
                    # send_keys('{ENTER}')
                    pyautogui.press('enter')
                    time.sleep(5)
                    # send_keys('{ENTER}')
                    pyautogui.press('enter')
                    time.sleep(10)

                    # espera_archivo(ruta_origen)
                    # # press('enter')
                    # # screenshot = ImageGrab.grab(bbox=None)
                    # # screenshot.save(r'G:\Mi unidad\Casos\Casos_Bono600\{}_01.png'.format(df['DNI'][i]), 'PNG')
                    ###Opcion 02
  
                    #Code to open the pop-up
                    # time.sleep(500)
                    # print('Antes del modals')
                    # driver.switch_to_frame("top")
                    # # driver.switch_to.frame(driver.find_element_by_id('top'))
                    # print('Despues del modals')

                    # a = driver.find_element_by_link_text("Abrir")
                    # a.click()
                    # time.sleep(500)
                    #ActionChains(driver).key_down(Keys.CONTROL).click(a).key_up(Keys.CONTROL).perform()
                    ####Opcion 03
                    
                    # time.sleep(500)
                    # actions = ActionChains(driver)
                    # actions.move_to_element_with_offset(driver.find_element_by_tag_name('body'), 0,0)
                    # print('Desde el 00')
                    # # time.sleep(500)
                    # actions.move_by_offset(931,761).click().perform()
                    # print('Desde el click')



                    print('En proceso del caso:{} del DNI:{}'.format(df['CASO'][i],df['DNI'][i]))

                    shutil.move(ruta_origen, ruta_destino)
                    os.rename(ruta_destino,ruta_new_nombre)
                    print('Terminando el con caso:{} del DNI:{}'.format(df['CASO'][i],df['DNI'][i]))
                    # pyautogui.click()
                    # time.sleep(5)
                    # pyautogui.moveTo(686, 248, 3)
                    # pyautogui.click()
                    # time.sleep(5)
                    # pyautogui.write(filepath)
                    # time.sleep(5)
                    # pyautogui.press('enter')
                    # screenshot = ImageGrab.grab(bbox=None)
                    # screenshot.save(r'G:\Mi unidad\Casos\Casos_Bono600\{}_02.png'.format(df['DNI'][i]), 'PNG')


                    #driver.find_element_by_text_link('Abrir').click()
                    #driver.find_element_by_xpath(pdf_download).click()
                except:
                    screenshot = ImageGrab.grab(bbox=None)
                    screenshot.save(filepath_png, 'PNG')
                    print(f'Error{traceback.format_exc()}')
            except:
                # time.sleep(500)
                # screenshot = ImageGrab.grab(bbox=None)
                # screenshot.save(filepath_png, 'PNG')
                print(f'Error {traceback.format_exc()}')
            
            driver.back()
            time.sleep(10)


def Actualizar_BD(tipo_bono,inicio,fin, caso = 'todos'):
    print('-'*80)
    try:
        bono = Datos_Bono(tipo_bono)
        df_bono = pd.read_excel(
            r'{ruta_bono}\{caso}_casos_{tipo_bono}_{inicio}-{fin}.xlsx'.format(
                ruta_bono=bono['ruta_bono'],
                tipo_bono=bono['bono'],
                caso='todos',
                inicio=inicio,
                fin=fin,
                ),
            sheet_name = 'Sheet1',
            skiprows = 4,
            usecols = 'A:AL')
        
        bd_bono = df_bono.fillna(' ')
        prueba = []

        #Oracle
        try:
            print('Oracle por Iniciar')
            cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_10")
        except:
            print('Oracle Iniciado')

        sql = config.sql

        connection = cx_Oracle.connect(
                config.username,
                config.password,
                config.dsn,
                encoding=config.encoding)
        # create a cursor
        cursor = connection.cursor()
        #Insert
        iteraciones = 0
        exito = 0
        error = 0
        tabla_error = []
        for index, row in bd_bono.iterrows():
            iteraciones += 1
            tb_valores= [
                row['TICKET'],
                row['DNI'],
                str(row['CELULAR']),
                str(row['CORREO']),
                str(row['CASO']),
                str(bono['sigla']),
                str(row['FECHA DE REGISTO']),
                str(row['DEPARTAMENTO']),
                row['ID'],
                str(row['APELLIDO PATERNO']),
                str(row['APELLIDO MATERNO']),
                str(row['NOMBRES']),
                str(row['BENEFICIARIO']),
                str(row['PROVINCIA']),
                str(row['DISTRITO']),
                str(row['LUGAR']),
                str(row['UBIGEO']),
                str(row['BANCO']),
                str(row['DNI CONTACTO']),
                str(row['APELLIDO PATERNO CONTACTO']),
                str(row['APELLIDO MATERNO CONTACTO']),
                str(row['NOMBRES CONTACTO']),
                str(row['CELULAR CONTACTO']),
                str(row['CORREO CONTACTO']),
                # row['DEPARTAMENTO PERCEPTOR'],
                # row['PROVINCIA PERCEPTOR'],
                # row['DISTRITO PERCEPTOR'],
                # row['UBIGEO PERCEPTOR'],
                str(row['CONSULTA']),
                str(row['REGISTRADOR']),
                str(row['ESTADO']),
                str(row['TIPO DE ATENCION']),
                str(row['EVALUADOR']),
                str(row['FECHA DE EVALUACION']),
                str(row['RESOLUCION DEL CASO']),
                str(row['CONCLUSIONES']),
                str(row['TIPO BONO']),
                # row['CODIGO ENTIDAD']
            ]
            try:
                cursor.execute(sql,tb_valores)
                connection.commit()
                #print(f"Actualizado item: {row['ID']} hora {datetime.now()}")
                exito += 1
            except:
                tabla_error.append(bd_bono.iloc[index])
                print(f'Error {traceback.format_exc()} in indice: {index}')
                error +=1
        
        #Guardando Archivo del Error
        df_error = pd.DataFrame(tabla_error)
        ruta_df_error = r'{ruta_bono}\{caso}_casos_{tipo_bono}_{inicio}-{fin}_error.csv'.format(
                ruta_bono=bono['ruta_bono'],
                tipo_bono=bono['bono'],
                caso='todos',
                inicio=inicio,
                fin=fin,
                )
        if len(df_error.index) > 0:
            df_error.to_csv(ruta_df_error,index = False, header=True)

        # Finalizando el comando
        print('==='*50)
        print('Resultado del Bono: {bono} en la fecha {date} se ha tenido exito: {exito} y error {error} de un total de {total}'.format(
            bono=bono['bono'],
            date=inicio,
            exito=exito,
            error=error,
            total=iteraciones
        ))
        print('==='*50)

        connection.close()

    except:
        print(f'Existe un error en el {tipo_bono}: {traceback.format_exc()}, tipo de casos:{caso}')
    print('-'*80)


###Versiones Actualizadas

def Iniciar_Sesion_Casos (driver,bono):
    try:
        #Variable Espera
        inicio = True
        contador = 1
        while inicio == True:
            #Inicios alternativos
            if contador % 2 != 0:
                driver.maximize_window()
                driver.get(bono['url'])
            else:
                driver.maximize_window()
                driver.get(url_alternativo)
            
            contador +=1

            #Acciones en la página
            driver.find_element_by_xpath(bono['path_user']).send_keys(bono['user'])
            driver.find_element_by_xpath(bono['path_pwd']).send_keys(bono['pwd'])
            time.sleep(5)
            driver.find_element_by_id('btnIngresar').click()
            time.sleep(15)
            print('Ingresando a la plataforma')
            try:
                driver.find_element_by_id('btnIngresar')
                print('Error en el ingreso, intentantando nuevamente')
                inicio = True
            except:
                print('Se accedio a la plataforma de forma satisfactoria')
                inicio = False
    except:
        print(traceback.format_exc())


def Descargar_Casos(tipo_bono,dias_anteriores,repeticiones,caso = 'todos'):
    print('-'*80)
    try:
        #Definición de Datos
        bono = Datos_Bono(tipo_bono)
        bono['ruta_origen'] = r'C:\Users\acastaneda\Downloads\reporte.xlsx'
        bono['datos_reporte'] = '//div[@id="tblDatos_info"]'
        bono['div_espera'] = '//div[@id="divEspera"]'

        #Iniciando Sesión
        driver = webdriver_chrome()
        print(f'Ingresando a la página del {tipo_bono}, tipo de casos:{caso}')
        Iniciar_Sesion_Casos(driver,bono)
        print(f'Logeo exitoso del {tipo_bono}, tipo de casos:{caso}')

        for i in range(dias_anteriores):
            #Variables
            var_fecha =date.today() - timedelta(days=dias_anteriores-i)
            bono['valor_date'] = var_fecha.strftime('%d%m%Y')
            bono['ruta_destino'] = r'{}\reporte.xlsx'.format(bono['ruta_bono'])
            bono['nombre_archivo'] = caso+"_casos_"+bono['bono']+"_"+bono['valor_date']+"-"+bono['valor_date']+".xlsx"
            bono['ruta_new_nombre'] = Path(bono['ruta_bono'],bono['nombre_archivo'])

            #Descarga de Casos
            print(f"Iniciando descarga del reporte de Fecha:{bono['valor_date']} - tipo de casos:{caso}")

            try:
                Descarga_Casos_iteraciones(driver,bono,tipo_bono,caso)
                Actualizar_BD(tipo_bono,bono['valor_date'],bono['valor_date'])
            except Exception as e:
                print(f"Fecha:{bono['valor_date']}-Existe un error en el {tipo_bono}: {traceback.format_exc()}, tipo de casos:{caso}")
            
            #Termino de repeticiones
            if i == repeticiones - 1:
                    break
        
        #Cerrar Sesión
        driver.quit()

    except Exception as e:
        print(f"Existe un error en el {tipo_bono}: {traceback.format_exc()}, tipo de casos:{caso}")
    
    print('-'*80)


def Descarga_Casos_iteraciones(driver,bono,tipo_bono,caso):
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
    
    espera_archivo(bono['ruta_origen'])

    shutil.move(bono['ruta_origen'], bono['ruta_destino'])
    os.rename(bono['ruta_destino'],bono['ruta_new_nombre'])

    print(f"Fecha:{bono['valor_date']}-Archivo movido del {tipo_bono} tipo de casos:{caso}")