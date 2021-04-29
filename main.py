#Python
from datetime import datetime

#Aplicaciones de los Bonos
from applications.bono.apps.descargar_insertar_casos import descargar_insertar_casos
from applications.bono.apps.actualizar_bd import actualizar_db
from applications.bono.apps.consolidar_insertar_casos import consolidar_insertar_casos
from tools.realizar_iteraciones import realizar_iteraciones


if __name__ == ('__main__'):
    # Bienvenida
    print("""
    Elegir la operación del bono a ejecutar
    Bono.1 Descarga Diaria de casos de bonos e insersión en la base de datos
    Bono.2 Descarga de PDFs
    Bono.3 Actualización masiva de reportes a la base de datos
    Bono.4 Actualización de la tabla CASOS BONOS
    """)

    comando = input("Elegir un comando : ")

    if comando == 'Bono.1' or comando == 'Bono.2' or comando == 'Bono.3' or comando == 'Bono.4':
        print('==='*50)

        #Iniciando Comando
        print(f'Iniciando comando: {comando} - hora {datetime.now()}')

        if comando == 'Bono.1':
            # var_fecha =date.today() - timedelta(days=8-1)
            # print(var_fecha)

            descargar_insertar_casos('Bono 600',1,1)
            descargar_insertar_casos('Bono BFU',1,1)
            descargar_insertar_casos('Bono RURAL',1,1)
            descargar_insertar_casos('Bono URBANO',1,1)

        elif comando == 'Bono.2':
            Descargar_adjunto('Bono 600','Deseo renunciar o devolver el bono', inicio = '04042021',fin= '04042021')

        elif comando == 'Bono.3':
            consolidar_insertar_casos(24,22)

        elif comando == 'Bono.4':
            realizar_iteraciones(4,1)


        print(f'Terminando comando: {comando} - hora {datetime.now()}')

    else:
        print('No se ha elegido ninguna opción')