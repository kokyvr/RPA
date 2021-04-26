#Librerias Python
import traceback
import time


def iniciar_sesion(driver,bono):
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
                driver.get(bono['url_alternativo'])
            
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