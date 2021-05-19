#Librerias Python
import traceback
from datetime import date
from datetime import timedelta
#Librerias Propias
from .datos_bono import datos_bono
from .iniciar_sesion import iniciar_sesion
from .descargar_web_adjunto import descargar_web_adjunto
from tools.webdriver_chrome import webdriver_chrome

def descargar_adjunto(tipo_bono,dias_anteriores,repeticiones):
    try:
        bono = datos_bono(tipo_bono)
        #Iniciando Sesión
        contador = 5
        while contador==5:
            driver = webdriver_chrome()
            print(f'Ingresando a la página del {tipo_bono}')
            contador = iniciar_sesion(driver,bono)
            print(f'Logeo exitoso del {tipo_bono}')

        for i in range(dias_anteriores):
            #Variables
            var_fecha =date.today() - timedelta(days=dias_anteriores-i)
            bono['valor_date'] = var_fecha.strftime('%d%m%Y')
            bono['div_espera'] = '//div[@id="divEspera"]'
            #Ejecución
            descargar_web_adjunto(driver,bono)
        
            #Termino de repeticiones
            if i == repeticiones - 1:
                    break
            
        #Cerrar Sesión
        driver.quit()
    except:
        print(f"Existe un error en el {tipo_bono}: {traceback.format_exc()}")
        
