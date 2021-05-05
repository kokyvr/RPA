#Librerias Python
import traceback
#Librerias Python - Oracle
import cx_Oracle

#Librerias Propias
from config import config

def ejecutar_consulta_bd(query,var_date,argumentos):
    print('-'*80)
    try:
        #Oracle
        try:
            print('Oracle por Iniciar')
            cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_10")
        except:
            print('Oracle Iniciado')

        connection = cx_Oracle.connect(
                config.username,
                config.password,
                config.dsn,
                encoding=config.encoding)
        # create a cursor
        cursor = connection.cursor()
        
        try:
            print("Ejecutando comando")

            if argumentos == 'SI':
                cursor.execute(query,{'var_date':var_date})
            else:
                cursor.execute(query)

            connection.commit()
            print("Terminando la ejecución del comando")
        except:
            print(f'Error {traceback.format_exc()} ')
        
        # cursor.close()
        connection.close()

    except:
        print(f'Existe un error: {traceback.format_exc()} del query : {query}')
    print('-'*80)
