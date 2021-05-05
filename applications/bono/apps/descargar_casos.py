#Librerias Python
import traceback
from datetime import date
from datetime import timedelta
from pathlib import Path

#Librerias Propias
from .datos_bono import datos_bono
from .iniciar_sesion import iniciar_sesion
from .descargar_web_casos import descargar_web_casos
from .insertar_casos import insertar_casos
from tools.webdriver_chrome import webdriver_chrome
from tools.webdriver_chrome_proxy import webdriver_chrome_proxy

def descargar_casos(tipo_bono,dias_anteriores,repeticiones,caso = 'todos'):
    print('-'*80)
    try:
        #Definición de Datos
        bono = datos_bono(tipo_bono)
        bono['ruta_origen'] = r'C:\Users\acastaneda\Downloads\reporte.xlsx'
        bono['datos_reporte'] = '//div[@id="tblDatos_info"]'
        bono['div_espera'] = '//div[@id="divEspera"]'

        #Iniciando Sesión
        contador = 5
        while contador==5:
            driver = webdriver_chrome()
            print(f'Ingresando a la página del {tipo_bono}, tipo de casos:{caso}')
            contador = iniciar_sesion(driver,bono)
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
                descargar_web_casos(driver,bono,tipo_bono,caso)
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


