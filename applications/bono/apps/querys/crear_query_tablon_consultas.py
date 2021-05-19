#Librerias Python
import os
from datetime import date
from datetime import datetime
from datetime import timedelta
#Librerias Propias
from tools.reemplazar_palabra_archivo import reemplazar_palabra_archivo




def crear_query_tablon_consultas():
    archivo_inicial = r'G:\Mi unidad\RPA_P65\src\query_actualizar_tablon_consultas_base_hoy.sql'
    archivo_final = r'G:\Mi unidad\RPA_P65\src\query_actualizar_tablon_consultas_hoy.sql'

    #Eliminado archivo reporte previo
    if os.path.isfile(archivo_final):
        print('Archivo previo encontrado para eliminar')
        os.remove(archivo_final)
    #Idnetificando el día
    palabra_inicial = ['FECHA_HOY','SEMANA',]
    var_fecha =date.today() - timedelta(days=1)
    #Identificando nombre periodo del reporte
    # onDay = lambda date, day: date + datetime.timedelta(days=(day-date.weekday()+7)%7)
   
    
    if datetime.today().weekday() <= 4:
        viernes_proximo = date.today() - timedelta(days=datetime.today().weekday()) + timedelta(days=4)
        viernes_anterior = date.today() - timedelta(days=datetime.today().weekday()) - timedelta(days=3)
    else:
        viernes_anterior = date.today() - timedelta(days=datetime.today().weekday()) + timedelta(days=4)
        viernes_proximo = date.today() - timedelta(days=datetime.today().weekday()) + timedelta(days=11)

    periodo = f"DEL {viernes_anterior.strftime('%d/%m')} AL {viernes_proximo.strftime('%d/%m')}"
    print(periodo)

    palabra_final = [var_fecha.strftime('%Y-%m-%d'),periodo,]

    reemplazar_palabra_archivo(archivo_inicial,archivo_final,palabra_inicial,palabra_final)
