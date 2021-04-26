#Librerias Python
import traceback
#Librerias Python - Oracle
import cx_Oracle

#Librerias Propias
from config import config

def ejecutar_consulta_bd(tipo_bono,query):
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
                cursor.execute(query)
                connection.commit()
            except:
                print(f'Error {traceback.format_exc()} ')
        
        connection.close()

    except:
        print(f'Existe un error en el {tipo_bono}: {traceback.format_exc()} del query : {query}')
    print('-'*80)
