#Python
import datetime
import calendar
import time
#Propias
from Tools import *
from Function.function import *

if __name__ == ('__main__'):
    # Bienvenida
    print("""
    Elegir la operación del bono a ejecutar
    Bono.1 Descarga Diario de Archivos de Bonos y actualización de base de datos
    Bono.2 Descarga Consolidado de Archivos de Bonos y actualización de base de datos
    Bono.3 Descarga de PDFs
    """)

    comando = input("Elegir un comando : ")

    if comando == 'Bono.1' or comando == 'Bono.2' or comando == 'Bono.3' or comando == 'Bono.4':
        print('==='*50)

        #Iniciando Comando
        print(f'Iniciando comando: {comando} - hora {datetime.now()}')

        if comando == 'Bono.1':
            Descargar_Casos('Bono 600',1,1)
            Descargar_Casos('Bono BFU',1,1)
            Descargar_Casos('Bono RURAL',1,1)
            Descargar_Casos('Bono URBANO',1,1)
        
        elif comando == 'Bono.2':
            dias_anteriores = 5
            repeticiones = 1

            for i in range(dias_anteriores):
                date =date.today() - timedelta(days=dias_anteriores-i)
                valor_date = date.strftime('%d%m%Y')

                #Descarga de Informes
                print('*'*80)
                # print(f'Iniciando descarga de informes del día: {valor_date} - hora {datetime.now()}')
                # Descargar_Informe('Bono 600',inicio = valor_date,fin= valor_date)
                # Descargar_Informe('Bono BFU',inicio = valor_date,fin= valor_date)
                Descargar_Informe('Bono RURAL',inicio = valor_date,fin= valor_date)
                # Descargar_Informe('Bono URBANO',inicio = valor_date,fin= valor_date)

                # #Actualización de las base de datos
                # print('*'*80)
                # print(f'Actualizando información a la base de datos: {valor_date} - hora {datetime.now()}')
                # Actualizar_BD('Bono 600',inicio = valor_date,fin= valor_date)
                # Actualizar_BD('Bono BFU',inicio = valor_date,fin= valor_date)
                # Actualizar_BD('Bono RURAL',inicio = valor_date,fin= valor_date)
                # Actualizar_BD('Bono URBANO',inicio = valor_date,fin= valor_date)

                # if i == repeticiones - 1:
                #     break

                # Descargar_pdf('Bono 600','Deseo renunciar o devolver el bono', inicio = valor_date,fin= valor_date)
                # Descargar_pdf('Bono BFU','Deseo renunciar o devolver el bono', inicio = valor_date,fin= valor_date)
                # Descargar_pdf('Bono RURAL','Deseo renunciar o devolver el bono', inicio = valor_date,fin= valor_date)
                # Descargar_pdf('Bono URBANO','Deseo renunciar o devolver el bono', inicio = valor_date,fin= valor_date)

        elif comando == 'Bono.3':
            #Descargar_Informe(tipo_bono='Bono 600',caso='Deseo renunciar o devolver el bono',inicio = yesterday,fin= yesterday)
            Descargar_pdf('Bono 600','Deseo renunciar o devolver el bono', inicio = '04042021',fin= '04042021')
            #Descargar_pdf(driver,'Denuncia', inicio,fin)

        elif comando == 'Bono.4':
            # var_fecha =date.today() - timedelta(days=8-1)
            # print(var_fecha)
            # Descargar_Casos('Bono 600',7,1)
            Descargar_Casos('Bono BFU',7,1)
            Descargar_Casos('Bono RURAL',7,1)
            Descargar_Casos('Bono URBANO',7,1)



        print(f'Terminando comando: {comando} - hora {datetime.now()}')

    else:
        print('No se ha elegido ninguna opción')
    