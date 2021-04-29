#Librerias Python
import traceback
from datetime import date
from datetime import timedelta
from pathlib import Path

#Librerias Propias
from .datos_bono import datos_bono
from .iniciar_sesion import iniciar_sesion
from .descargar_casos import descargar_casos
from .insertar_casos import insertar_casos
from tools.webdriver_chrome import webdriver_chrome

def consolidar_insertar_casos(dias_anteriores,repeticiones,caso = 'todos'):
    print('='*80)
    try:
        for i in range(dias_anteriores):
            lst_bono = ['Bono 600','Bono BFU','Bono RURAL','Bono URBANO']
            var_fecha =date.today() - timedelta(days=dias_anteriores-i)
            print(f'{var_fecha}')

            print('-'*80)
            for tipo_bono in lst_bono:
                print(tipo_bono)

                #Definición de Datos
                bono = datos_bono(tipo_bono)

                #Variables
                bono['valor_date'] = var_fecha.strftime('%d%m%Y')

                #Actualización de Casos
                print(f"Iniciando actualización de la BD del reporte de Fecha:{bono['valor_date']} - tipo de casos:{caso}")

                try:
                    insertar_casos(tipo_bono,bono['valor_date'],bono['valor_date'])
                except Exception as e:
                    print(f"Fecha:{bono['valor_date']}-Existe un error en el {tipo_bono}: {traceback.format_exc()}, tipo de casos:{caso}")
                
                #Termino de repeticiones
            print('-'*80)
            if i == repeticiones - 1:
                break


    except Exception as e:
        print(f"Existe un error: {traceback.format_exc()}, tipo de casos:{caso}")
    
    print('='*80)


