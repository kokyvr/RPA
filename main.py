#Python
from datetime import datetime

#Aplicaciones de los Bonos
from applications.bono.apps.descargar_insertar_casos import descargar_insertar_casos


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
            # var_fecha =date.today() - timedelta(days=8-1)
            # print(var_fecha)
            descargar_insertar_casos('Bono 600',9,9)
            descargar_insertar_casos('Bono BFU',9,9)
            descargar_insertar_casos('Bono RURAL',9,9)
            descargar_insertar_casos('Bono URBANO',9,9)


        elif comando == 'Bono.2':
            Descargar_adjunto('Bono 600','Deseo renunciar o devolver el bono', inicio = '04042021',fin= '04042021')

        print(f'Terminando comando: {comando} - hora {datetime.now()}')

    else:
        print('No se ha elegido ninguna opción')