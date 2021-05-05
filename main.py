#Python
from datetime import datetime

#Aplicaciones de los Bonos
from applications.bono.apps.actualizar_bd import actualizar_db
from applications.bono.apps.consolidar_insertar_casos import consolidar_insertar_casos
from applications.bono.apps.consolidar_descargar_casos import consolidar_descargar_casos
from tools.realizar_iteraciones import realizar_iteraciones


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

    if comando == 'Bono.1' or comando == 'Bono.2' or comando == 'Bono.3' or comando == 'Bono.4':
        print('==='*50)

        #Iniciando Comando
        print(f'Iniciando comando: {comando} - hora {datetime.now()}')

        if comando == 'Bono.1':
            consolidar_descargar_casos(1,1)
            consolidar_insertar_casos(1,1)

        elif comando == 'Bono.2':
            consolidar_descargar_casos(6,5)

        elif comando == 'Bono.3':
            consolidar_insertar_casos(29,29)

        elif comando == 'Bono.4':
            Descargar_adjunto('Bono 600','Deseo renunciar o devolver el bono', inicio = '04042021',fin= '04042021')

        elif comando == 'Bono.5':
            realizar_iteraciones(7,1)


        print(f'Terminando comando: {comando} - hora {datetime.now()}')

    else:
        print('No se ha elegido ninguna opción')