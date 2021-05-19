#Librerias Python
import traceback
import time
import pickle
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from tools.webdriver_chrome import webdriver_chrome

def iniciar_sesion(driver,bono):
    try:
        #Variable Espera
        inicio = True
        contador = 1
        while inicio == True:
            # cookies = pickle.load(open("cookies.pkl", "rb"))
            # for cookie in cookies:
            #     driver.add_cookie(cookie)

            #Inicios alternativos
            if contador == 1:
                driver.maximize_window()
                driver.get(bono['url'])
                time.sleep(5)
                driver.refresh()
                time.sleep(5)
            elif contador == 5:
                return contador
                break
            elif contador % 2 == 0:
                a = ActionChains(driver)
                a.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()
                time.sleep(5)
            elif contador % 3 == 0:
                driver.maximize_window()
                driver.get(bono['url_alternativo'])
                driver.refresh()
                time.sleep(5)
            else:
                driver.maximize_window()
                driver.get(bono['url'])
                time.sleep(5)
                driver.refresh()
                time.sleep(5)

            contador +=1

            #Acciones en la página
            try:
                driver.find_element_by_xpath('//button[@id="details-button"]').click()
                driver.find_element_by_xpath('//a[@id="proceed-link"]').click()
                print('Sin certificado de Seguridad')
            except:
                print('Con certificado de Seguridad')

            driver.find_element_by_xpath(bono['path_user']).send_keys(bono['user'])
            driver.find_element_by_xpath(bono['path_pwd']).send_keys(bono['pwd'])
            time.sleep(5)
            driver.find_element_by_id('btnIngresar').click()
            time.sleep(15)
            print('Ingresando a la plataforma')
            pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
            try:
                driver.find_element_by_id('btnIngresar')
                print('Error en el ingreso, intentantando nuevamente')
                inicio = True
            except:
                print('Se accedio a la plataforma de forma satisfactoria')
                inicio = False
    except:
        print(traceback.format_exc())