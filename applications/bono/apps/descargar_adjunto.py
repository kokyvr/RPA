def descargar_adjunto(tipo_bono,caso,inicio,fin):
    time.sleep(10)

    # pyautogui.FAILSAFE = False
    bono = Datos_Bono(tipo_bono)
    df = pd.read_excel(
        r'{ruta_bono}\{caso}_casos_{tipo_bono}_{inicio}-{fin}.xlsx'.format(
            ruta_bono=bono['ruta_bono'],
            tipo_bono=bono['bono'],
            caso='todos',
            inicio=inicio,
            fin=fin,
            ),
        sheet_name = 'Sheet1',
        skiprows = 4,
        usecols = 'A:AL')
    
    #url_user= 'https://casos.bono600.gob.pe/intranet_/?c=Registro&a=Editar&i={}'.format(df['ID'][0])
    field_search = '//div[@id="tblDatos_filter"]/label/input'
    btn_editar = '//button[@title="Editar"]'
    div_espera = '//div[@id="divEspera"]'
    ruta_origen = r'C:\Users\acastaneda\Downloads\descarga.pdf'
    ruta_destino = r'{ruta_bono}\{caso}\descarga.pdf'.format(
                                ruta_bono=bono['ruta_bono'],
                                caso=caso,
                                )

     
    #Iniciando Sesión
    driver = webdriver_chrome()
    print(f'Ingresando a la página del {tipo_bono}, tipo de casos:{caso}')
    iniciar_sesion(driver,bono['url'],bono['url_alternativo'],bono['pwd'],bono['path_pwd'],bono['user'],bono['path_user'])
    print(f'Logeo exitoso del {tipo_bono}, tipo de casos:{caso} ')
    # Ingresar al listado de casos 
    driver.find_element_by_xpath(bono['field_start_date']).send_keys(inicio)
    driver.find_element_by_xpath(bono['field_end_date']).send_keys(fin)
    time.sleep(5)
    driver.find_element_by_xpath(bono['btn_actualizar']).click()
    WebDriverWait(driver,100).until(EC.invisibility_of_element_located((By.XPATH, div_espera)))
    time.sleep(5)
    print('Número de elementos {}'.format(len(df)))
    for i in range(len(df)):
        if str(df['CASO'][i]) == caso :
            print('Iniciando el con caso:{} del DNI:{}'.format(df['CASO'][i],df['DNI'][i]))
            try:
                ruta_new_nombre = r'{ruta_bono}\{caso}\{nro}_{fecha}_{dni}.pdf'.format(
                                ruta_bono=bono['ruta_bono'],
                                caso=caso,
                                nro = str(df['Nro.'][i]),
                                fecha=inicio,
                                dni=str(df['DNI'][i]),
                                )
                filepath_png = r'{ruta_bono}\{caso}\{nro}_{fecha}_{dni}.png'.format(
                                ruta_bono=bono['ruta_bono'],
                                caso=caso,
                                nro = str(df['Nro.'][i]),
                                fecha=inicio,
                                dni=str(df['DNI'][i]),
                                )

                #Seleccionar DNI específico
                driver.find_element_by_xpath(field_search).send_keys(str(df['DNI'][i]))
                time.sleep(5)
                #Editar Valor
                driver.find_element_by_xpath(btn_editar).click()
                time.sleep(5)
                #Descargando archivos
                try:
                    driver.find_element_by_id('btnDoc1').click()
                    time.sleep(5)
                    #### Opcion 01
                    # pywinauto.mouse.click(button='left', coords=(931,761))
                    pywinauto.mouse.click(button='right', coords=(1159,551))
                    # pyautogui.click(button='right',x=1159, y=551)
                    time.sleep(5)
                    # send_keys('{DOWN}')
                    pyautogui.press('down')
                    time.sleep(5)
                    # send_keys('{ENTER}')
                    pyautogui.press('enter')
                    time.sleep(5)
                    # send_keys('{ENTER}')
                    pyautogui.press('enter')
                    time.sleep(10)

                    # espera_archivo(ruta_origen)
                    # # press('enter')
                    # # screenshot = ImageGrab.grab(bbox=None)
                    # # screenshot.save(r'G:\Mi unidad\Casos\Casos_Bono600\{}_01.png'.format(df['DNI'][i]), 'PNG')
                    ###Opcion 02
  
                    #Code to open the pop-up
                    # time.sleep(500)
                    # print('Antes del modals')
                    # driver.switch_to_frame("top")
                    # # driver.switch_to.frame(driver.find_element_by_id('top'))
                    # print('Despues del modals')

                    # a = driver.find_element_by_link_text("Abrir")
                    # a.click()
                    # time.sleep(500)
                    #ActionChains(driver).key_down(Keys.CONTROL).click(a).key_up(Keys.CONTROL).perform()
                    ####Opcion 03
                    
                    # time.sleep(500)
                    # actions = ActionChains(driver)
                    # actions.move_to_element_with_offset(driver.find_element_by_tag_name('body'), 0,0)
                    # print('Desde el 00')
                    # # time.sleep(500)
                    # actions.move_by_offset(931,761).click().perform()
                    # print('Desde el click')



                    print('En proceso del caso:{} del DNI:{}'.format(df['CASO'][i],df['DNI'][i]))

                    shutil.move(ruta_origen, ruta_destino)
                    os.rename(ruta_destino,ruta_new_nombre)
                    print('Terminando el con caso:{} del DNI:{}'.format(df['CASO'][i],df['DNI'][i]))
                    # pyautogui.click()
                    # time.sleep(5)
                    # pyautogui.moveTo(686, 248, 3)
                    # pyautogui.click()
                    # time.sleep(5)
                    # pyautogui.write(filepath)
                    # time.sleep(5)
                    # pyautogui.press('enter')
                    # screenshot = ImageGrab.grab(bbox=None)
                    # screenshot.save(r'G:\Mi unidad\Casos\Casos_Bono600\{}_02.png'.format(df['DNI'][i]), 'PNG')


                    #driver.find_element_by_text_link('Abrir').click()
                    #driver.find_element_by_xpath(pdf_download).click()
                except:
                    screenshot = ImageGrab.grab(bbox=None)
                    screenshot.save(filepath_png, 'PNG')
                    print(f'Error{traceback.format_exc()}')
            except:
                # time.sleep(500)
                # screenshot = ImageGrab.grab(bbox=None)
                # screenshot.save(filepath_png, 'PNG')
                print(f'Error {traceback.format_exc()}')
            
            driver.back()
            time.sleep(10)