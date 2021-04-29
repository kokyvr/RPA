
def datos_bono(bono):
    my_dict_bono = {}
    if bono == 'Bono BFU':
        #Insertar datos al dictionario my_dict_bono
        my_dict_bono['sigla'] = 'BFU'
        my_dict_bono['bono'] = 'Bono BFU'
        my_dict_bono['user'] = '07266464'
        my_dict_bono['pwd'] = 'L@urdes2013'
        my_dict_bono['ruta_bono'] = r'G:\Mi unidad\Casos\Casos_BFU'
        my_dict_bono['url'] = 'https://casos.bfu.gob.pe/intranet_/index.php'
        my_dict_bono['url_alternativo'] = 'https://casos.bfu.gob.pe/intranet_/'
        my_dict_bono['path_user'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[1]/input'
        my_dict_bono['path_pwd'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[2]/input'
        my_dict_bono['btn_enter'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[3]/input'
        my_dict_bono['btn_actualizar'] = '//button[@id="btnMostrar"]'
        my_dict_bono['field_start_date'] = '//input[@id="txtFechaConsulta"]'
        my_dict_bono['field_end_date'] = '//input[@id="txtFechaConsultaFin"]'
        my_dict_bono['btn_exportar'] = '//button[@id="btnExportarRegistrosFecha"]'
        
    elif bono == 'Bono RURAL':
        my_dict_bono['sigla'] = 'RURAL'
        my_dict_bono['bono'] = 'Bono RURAL'
        #Insertar datos al dictionario my_dict_bono
        my_dict_bono['user'] = '07266464'
        my_dict_bono['pwd'] = 'L@urdes2013'
        my_dict_bono['ruta_bono'] = r'G:\Mi unidad\Casos\Casos_RURAL'
        my_dict_bono['url'] = 'https://consultas.bonorural.pe/intranet_/'
        my_dict_bono['url_alternativo'] = 'https://consultas.bonorural.pe/intranet_/index.php'
        my_dict_bono['path_user'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[1]/input'
        my_dict_bono['path_pwd'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[2]/input'
        my_dict_bono['btn_enter'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[4]/input'
        my_dict_bono['btn_actualizar'] = '//button[@id="btnMostrar"]'
        my_dict_bono['field_start_date'] = '//input[@id="txtFechaConsulta"]'
        my_dict_bono['field_end_date'] = '//input[@id="txtFechaConsultaFin"]'
        my_dict_bono['btn_exportar'] = '//button[@id="btnExportarRegistrosFecha"]'

    elif bono == 'Bono URBANO':
        #Insertar datos al dictionario my_dict_bono
        my_dict_bono['sigla'] = 'URBANO'
        my_dict_bono['bono'] = 'Bono URBANO'
        my_dict_bono['user'] = '07266464'
        my_dict_bono['pwd'] = 'L@urdes2013'
        my_dict_bono['ruta_bono'] = r'G:\Mi unidad\Casos\Casos_URBANO'
        #URL
        my_dict_bono['url'] = 'https://consultas.yomequedoencasa.pe/intranet_/'
        my_dict_bono['url_alternativo'] = 'https://consultas.yomequedoencasa.pe/intranet_/index.php'
        #XPATH
        my_dict_bono['path_user'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[1]/input'
        my_dict_bono['path_pwd'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[2]/input'
        my_dict_bono['btn_enter'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[4]/input'
        my_dict_bono['btn_actualizar'] = '//button[@id="btnMostrar"]'
        my_dict_bono['field_start_date'] = '//input[@id="txtFechaConsulta"]'
        my_dict_bono['field_end_date'] = '//input[@id="txtFechaConsultaFin"]'
        my_dict_bono['btn_exportar'] = '//button[@id="btnExportarRegistrosFecha"]'

    elif bono == 'Bono 600':
        #Insertar datos al dictionario my_dict_bono
        my_dict_bono['sigla'] = '600'
        my_dict_bono['bono'] = 'Bono 600'
        my_dict_bono['user'] = '07266464'
        my_dict_bono['pwd'] = 'L@urdes2013'
        my_dict_bono['ruta_bono'] = r'G:\Mi unidad\Casos\Casos_Bono600'
        #URL
        my_dict_bono['url'] = 'https://casos.bono600.gob.pe/intranet_/index.php'
        my_dict_bono['url_alternativo'] = 'https://casos.bono600.gob.pe/intranet_/'
        #XPATH
        my_dict_bono['path_user'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[1]/input'
        my_dict_bono['path_pwd']= '/html/body/div[1]/div/div/div/article/div/div/div/form/div[2]/input'
        my_dict_bono['btn_enter'] = '/html/body/div[1]/div/div/div/article/div/div/div/form/div[3]/input'
        my_dict_bono['btn_actualizar'] = '//button[@id="btnMostrar"]'
        my_dict_bono['field_start_date'] = '//input[@id="txtFechaConsulta"]'
        my_dict_bono['field_end_date'] = '//input[@id="txtFechaConsultaFin"]'
        my_dict_bono['btn_exportar'] = '//button[@id="btnExportarRegistrosFecha"]'
    else:
        print('Error en la digitación')
    return my_dict_bono
