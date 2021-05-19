#Python
import os

# import time
# import sys
# import os, shutil
# import smtplib
# import win32com.client
# from datetime import date
# from datetime import timedelta
# from pathlib import Path
# import traceback
# from PIL import ImageGrab
# import pyautogui
# from keyboard import press
# #Pywinauto
# import pywinauto
# from pywinauto.keyboard import send_keys
# #Selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains
# #Pandas
# import pandas as pd
# #Oracle
# import cx_Oracle
# from applications.bono.apps.actualizar_bd import *
# from applications.bono.apps.datos_bono import *
# from applications.bono.apps.descargar_adjunto import *
# from applications.bono.apps.descargar_casos import *
# from applications.bono.apps.iniciar_sesion import *
# from applications.bono.apps.insertar_casos import *

# Tools
# from tools.espera_archivo import *
# from tools.webdriver_chrome import *

# from applications.bono.apps import *
# sys.path.append(".")
# from tools import *

#Datos del Correo
mail_user = 'contratista02@pension65.gob.pe'
mail_pass = 'tribich.123'



#Conexión a Oracle
cxn_oracle = r"C:\instantclient_19_10"

#WebDriver
cxn_oracle = r'C:\chromedriver/chromedriver.exe'

#Google Drive
llave_json = r"{}\config\llave.json".format(os.path.dirname(os.path.dirname(__file__)))

#Datos de la Base de Datos
username = 'user_apoyo1'
password = 'Fortinate2017'
dsn = '10.10.10.6/p65dbprd'
port = 1521
encoding = 'UTF-8'

#Estructura de la Base de Datos
sql = """ insert into CASOS_BONOS(
            TICKET,
            DNI,
            CELULAR,
            CORREO,
            CASO,
            NOMBRE_BONO,
            FECHA_REGISTRO,
            DEPARTAMENTO,
            ID_CONSULTA,
            "APELLIDO PATERNO",
            "APELLIDO MATERNO",
            NOMBRES,
            BENEFICIARIO,
            PROVINCIA,
            DISTRITO,
            LUGAR,
            UBIGEO,
            BANCO,
            "DNI CONTACTO",
            "APELLIDO PATERNO CONTACTO",
            "APELLIDO MATERNO CONTACTO",
            "NOMBRES CONTACTO",
            "CELULAR CONTACTO",
            "CORREO CONTACTO",
            CONSULTA,
            REGISTRADOR,
            ESTADO,
            "TIPO DE ATENCION",
            EVALUADOR,
            "FECHA DE EVALUACION",
            "RESOLUCION DEL CASO",
            CONCLUSIONES,
            "TIPO BONO"
        )
        values(
            :02,
            :03,
            :04,
            :05,
            :06,
            :07,
            :08,
            :09,
            :10,
            :11,
            :12,
            :13,
            :14,
            :15,
            :16,
            :17,
            :18,
            :19,
            :20,
            :21,
            :22,
            :23,
            :24,
            :25,
            :26,
            :27,
            :28,
            :29,
            :30,
            :31,
            :32,
            :33,
            :34
        ) """
sql_completo = """ insert into CASOS_BONOS(
            TICKET,
            DNI,
            CELULAR,
            CORREO,
            CASO,
            NOMBRE_BONO,
            FECHA_REGISTRO,
            DEPARTAMENTO,
            ID_CONSULTA,
            "APELLIDO PATERNO",
            "APELLIDO MATERNO",
            NOMBRES,
            BENEFICIARIO,
            PROVINCIA,
            DISTRITO,
            LUGAR,
            UBIGEO,
            BANCO,
            "DNI CONTACTO",
            "APELLIDO PATERNO CONTACTO",
            "APELLIDO MATERNO CONTACTO",
            "NOMBRES CONTACTO",
            "CELULAR CONTACTO",
            "CORREO CONTACTO",
            "DEPARTAMENTO PERCEPTOR",
            "PROVINCIA PERCEPTOR",
            "DISTRITO PERCEPTOR",
            "UBIGEO PERCEPTOR",
            CONSULTA,
            REGISTRADOR,
            ESTADO,
            "TIPO DE ATENCION",
            EVALUADOR,
            "FECHA DE EVALUACION",
            "RESOLUCION DEL CASO",
            CONCLUSIONES,
            "TIPO BONO",
            "CODIGO ENTIDAD"
        )
        values(
            :02,
            :03,
            :04,
            :05,
            :06,
            :07,
            :08,
            :09,
            :10,
            :11,
            :12,
            :13,
            :14,
            :15,
            :16,
            :17,
            :18,
            :19,
            :20,
            :21,
            :22,
            :23,
            :24,
            :25,
            :26,
            :27,
            :28,
            :29,
            :30,
            :31,
            :32,
            :33,
            :34,
            :35,
            :36,
            :37,
            :38,
            :39
        ) """
