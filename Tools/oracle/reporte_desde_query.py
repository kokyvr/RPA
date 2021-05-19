#Librerias Python
import traceback
#Librerias Python - Oracle
import cx_Oracle
#Librerias Python - Pandas
import pandas as pd
#Librerias Propias
from config import config


def reporte_desde_query(query,file):
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

    df = pd.read_sql(query, con=connection)
    path_file = r'G:\Mi unidad\Casos\Reportes\{}.xlsx'.format(file)
    df.to_excel(path_file, sheet_name=file, index = False)

    return len(df)