#Librerias Python
import traceback
import shutil
import os
import csv
#Librerias Python - Oracle
import cx_Oracle
#Librerias Python - Pandas
import pandas as pd
#Librerias Propias
from config import config



def save_df(df, chunk_size=5000):
    df_size=len(df)
    ruta = 'G:\\Mi unidad\\Casos\\Mensajes\\'
    if os.path.isfile(ruta):
        shutil.rmtree(ruta)
    for i, start in enumerate(range(0, df_size, chunk_size)):
        df[start:start+chunk_size].to_csv(
            r'{}df_mensaje_{}.csv'.format(ruta,i),
            sep=';',
            index = False, 
            header=True,
            encoding = 'latin-1')

def obtener_csv_oracle(tipo_bono):
    #Oracle
    try:
        print('Oracle por Iniciar')
        cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_10")
    except:
        print('Oracle Iniciado')

    query = """select 
            ID_CONSULTA AS "ID_CONSULTA",
            MENSAJE,
            '72385282' AS "DNI",
            RESULTADO_MENSAJE_CODIGO AS "ESTADO"
            from USER_APOYO1.CASOS_BONOS 
            WHERE 
            TIPO_CASOS != 'Beneficiario no reconoce a perceptor del bono' and ID_CONSULTA IS NOT NULL AND 
            NOMBRE_BONO = '{}'""".format(tipo_bono)

    connection = cx_Oracle.connect(
            config.username,
            config.password,
            config.dsn,
            encoding=config.encoding)

    df = pd.read_sql(query, con=connection)
    save_df(df)