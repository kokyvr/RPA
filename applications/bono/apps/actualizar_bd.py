#Librerias Python
import traceback
#Librerias Python - Pandas
import pandas as pd
#Librerias Propias
from tools.ejecutar_consulta_bd import ejecutar_consulta_bd


def actualizar_db(var_date):
    df_query = pd.read_excel(
        r'G:\Mi unidad\RPA_P65\src\querys.xlsx',
        sheet_name = 'query',
        usecols = 'A:D')

    var_date_query = f'{var_date}%'

    for index, row in df_query.iterrows():
        try:
            print('*'*80)
            print(f"Iniciando query: comando-{row['Comando']} para la columna {row['Columna']} con fecha {var_date}")
            query = row['Query']

            if row['Argumentos'] == 'SI':
                ejecutar_consulta_bd(query=query,var_date=var_date_query,argumentos='SI')
            else:
                ejecutar_consulta_bd(query=query,var_date=var_date_query,argumentos = 'NO')
            
            print(f"Finalizando query: comando-{row['Comando']} para la columna {row['Columna']} con fecha {var_date}")
            print('*'*80)
        except:
            print(f'Existe un error: {traceback.format_exc()}')
