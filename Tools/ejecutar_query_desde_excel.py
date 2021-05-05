#Librerias Python
import traceback
#Librerias Python - Pandas
import pandas as pd
#Librerias Propias
from tools.ejecutar_consulta_bd import ejecutar_consulta_bd


def ejecutar_query_desde_excel(var_date,hoja,rango):
    df_query = pd.read_excel(
        r'G:\Mi unidad\RPA_P65\src\querys.xlsx',
        sheet_name = hoja,
        usecols = rango)

    var_date_query = f'{var_date}%'

    var_exito = 0
    var_error = 0
    var_total = 0

    for index, row in df_query.iterrows():
        var_total += 1
        try:
            print('_'*80)
            print(f"Iniciando query: comando-{row['Comando']} para la columna {row['Columna']} con fecha {var_date}")
            query = str(row['Query'])

            print(query)
            
            if row['Estado'] == 'OK':
                if row['Argumentos'] == 'SI':
                    try:
                        ejecutar_consulta_bd(query=query,var_date=var_date_query,argumentos='SI')
                        var_exito += 1
                    except:
                        var_error += 1

                else:
                    try:
                        ejecutar_consulta_bd(query=query,var_date=var_date_query,argumentos='NO')
                        var_exito += 1
                    except:
                        var_error += 1
            
            print(f"Finalizando query: comando-{row['Comando']} para la columna {row['Columna']} con fecha {var_date}")
            print('_'*80)
        except:
            print(f'Existe un error: {traceback.format_exc()}')
    
    print('*'*80)
    print(f'Total de Casos:{var_total}, número de éxitos:{var_exito} y número de errores:{var_error}')
    print('*'*80)
