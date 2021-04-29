#Librerias Python
from selenium import webdriver


def webdriver_chrome():
    #Webdriver
    ruta_chromedriver = 'C:\chromedriver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=ruta_chromedriver)

    return driver



