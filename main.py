#Python
from datetime import datetime

#Aplicaciones de los Bonos
from applications.bono.apps.actualizar_bd import actualizar_db
from applications.bono.apps.registrar_original_bd import registrar_original_bd
from applications.bono.apps.consolidar_insertar_casos import consolidar_insertar_casos
from applications.bono.apps.consolidar_descargar_casos import consolidar_descargar_casos
from applications.bono.apps.consolidar_importar_mensajes import consolidar_importar_mensajes
from applications.bono.apps.consolidar_descargar_adjuntos import consolidar_descargar_adjuntos
from applications.bono.apps.descargar_adjunto_por_informe import descargar_adjunto_por_informe
from applications.bono.apps.reportes.extornos_planillas import extornos
from applications.bono.apps.reportes.extornos_planillas import planillas
from applications.bono.apps.casos_rdd.actualizar_sheet_rdd import actualizar_sheet_rdd
from applications.bono.apps.crear_archivo_query_hoy import crear_archivo_query_hoy
from applications.bono.apps.querys.crear_query_tablon_consultas import crear_query_tablon_consultas
from tools.realizar_iteraciones import realizar_iteraciones
from tools.google_drive.actualizar_google_drive import actualizar_google_drive




if __name__ == ('__main__'):
    # Bienvenida
    print("""
    Elegir la operación del bono a ejecutar
    Bono.1 Descarga Diaria de casos de bonos e insersión en la base de datos
    Bono.2 Descarga masiva de reportes de Casos
    Bono.3 Actualización masiva de reportes a la base de datos
    Bono.4 Descarga de Adjuntos
    Bono.5 Actualización de la tabla CASOS BONOS
    """)

    comando = input("Elegir un comando : ")

    if  (comando == 'Bono.1' or 
        comando == 'Bono.2' or 
        comando == 'Bono.3' or 
        comando == 'Bono.4' or 
        comando == 'Bono.5' or 
        comando == 'Bono.6' or
        comando == 'Bono.7' or
        comando == 'Bono.8'):
        print('==='*50)

        #Iniciando Comando
        print(f'Iniciando comando: {comando} - hora {datetime.now()}')

        if comando == 'Bono.1':
            consolidar_descargar_casos(1,1)
            consolidar_insertar_casos(1,1)
            crear_archivo_query_hoy()
            crear_query_tablon_consultas()

        elif comando == 'Bono.2':
            consolidar_descargar_casos(6,5)

        elif comando == 'Bono.3':
            consolidar_insertar_casos(29,29)

        elif comando == 'Bono.4':
            # consolidar_descargar_adjuntos(37,37)
            #  descargar_adjunto_por_informe('Bono 600','Deseo renunciar o devolver el bono','22042021','10052021')
            descargar_adjunto_por_informe('Bono 600','Registre su denuncia por suplantación','07102020','10052021')
            #  descargar_adjunto_por_informe('Bono BFU','Deseo renunciar o devolver el bono','07102020','10052021')
            #  descargar_adjunto_por_informe('Bono BFU','Registre su denuncia por suplantación','07102020','10052021')


        elif comando == 'Bono.5':
            realizar_iteraciones(7,1)

        elif comando == 'Bono.6':
            consolidar_importar_mensajes()

        elif comando == 'Bono.7':
            extornos()
            planillas()

        elif comando == 'Bono.8':
            # actualizar_google_drive("1BV7Lhz_SFHDYLIyo-xGzgrdbY6vSISRXBuhFIQcDgjA", "BD",[1,2,3],["Hola Mundo","Hi","Helllo!",])
            # actualizar_sheet_rdd()
            crear_query_tablon_consultas()


        print(f'Terminando comando: {comando} - hora {datetime.now()}')

    else:
        print('No se ha elegido ninguna opción')