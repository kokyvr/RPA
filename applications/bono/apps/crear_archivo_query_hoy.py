#Librerias Python
import os
from datetime import date
from datetime import timedelta
#Librerias Propias
from tools.reemplazar_palabra_archivo import reemplazar_palabra_archivo

def crear_archivo_query_hoy():
    archivo_inicial = r'G:\Mi unidad\RPA_P65\src\query_actualizar_bd_base_hoy.sql'
    archivo_final = r'G:\Mi unidad\RPA_P65\src\query_actualizar_bd_hoy.sql'

    #Eliminado archivo reporte previo
    if os.path.isfile(archivo_final):
        print('Archivo previo encontrado para eliminar')
        os.remove(archivo_final)

    palabra_inicial = 'FECHA_HOY'
    var_fecha =date.today() - timedelta(days=1)
    palabra_final = var_fecha.strftime('%Y-%m-%d')

    reemplazar_palabra_archivo(archivo_inicial,archivo_final,palabra_inicial,palabra_final)
