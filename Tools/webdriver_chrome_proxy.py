#Librerias Python
from selenium import webdriver
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

def webdriver_chrome_proxy():

    # req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
    # proxies = req_proxy.get_proxy_list() #this will create proxy list
    # ind = [] #int is list of Indian proxy
    # for proxy in proxies:
    #     if proxy.country == 'Peru':
    #         ind.append(proxy.get_address())

    # PROXY = ind[0]
    # print(PROXY)
    # webdriver.DesiredCapabilities.CHROME['proxy']={
    #     "httpProxy":PROXY,
    #     "ftpProxy":PROXY,
    #     "sslProxy":PROXY,
    #     "proxyType":"MANUAL",
    # }
    
    #Webdriver
    # options = Options()
    # ua = UserAgent()
    # userAgent = ua.random
    # print(userAgent)
    # options.add_argument(f'user-agent={userAgent}')
    # driver = webdriver.Chrome(executable_path=ruta_chromedriver,chrome_options=options)
    
    #Webdriver
    ruta_chromedriver = 'C:\chromedriver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=ruta_chromedriver)

    return driver

