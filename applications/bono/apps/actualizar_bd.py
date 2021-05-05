#Librerias Python
import traceback
#Librerias Python - Pandas
import pandas as pd
#Librerias Propias
from tools.ejecutar_consulta_bd import ejecutar_consulta_bd
from tools.ejecutar_query_desde_excel import ejecutar_query_desde_excel



def actualizar_db(var_date):
    #Consulta Diaria
    # ejecutar_query_desde_excel(var_date,'query_original','A:I')
    ejecutar_query_desde_excel(var_date,'casos','A:H')
    # ejecutar_query_desde_excel(var_date,'codigo_casos','A:H')

    #Consulta Gobales
    # ejecutar_query_desde_excel(var_date,'mensajes','A:X')
    # ejecutar_query_desde_excel(var_date,'query_actual','A:I')
