import cx_Oracle
import time
from datetime import datetime 
import pandas as pd
from datetime import datetime
#Modulos Externos
import config

def insert_oracle(ID,TICKET,DNI,CELULAR,CORREO,CASO,NOMBRE_BONO):
    """
    Insert a row to the billing_headers table
    :param billing_date:
    :param amount:
    :param customer_id:
    :param note:
    :return:
    """
    # construct an insert statement that add a new row to the billing_headers table
    sql = ('insert into CASOS_BONOS(ID,TICKET,DNI,CELULAR,CORREO,CASO,NOMBRE_BONO) '
        'values(:ID,:TICKET,:DNI,:CELULAR,:CORREO,:CASO,:NOMBRE_BONO)')

    try:
        # establish a new connection
        
        cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_10")
        with cx_Oracle.connect(
            config.username,
            config.password,
            config.dsn,
            encoding=config.encoding) as connection:
            # create a cursor
            with connection.cursor() as cursor:
                # execute the insert statement
                cursor.execute(sql, [ID,TICKET,DNI,CELULAR,CORREO,CASO,NOMBRE_BONO])
                # commit work
                connection.commit()
            
        print('Actualizado correctamente')
        connection.close()
    except cx_Oracle.Error as error:
        print('Error occurred:')
        print(error)


if __name__ == '__main__':
    # df_bono = pd.read_csv(r'C:\Users\acastaneda\Downloads\prueba.csv',sep=';',nrows= 1,encoding = "ISO-8859-1",low_memory=False)
    #df_bono = pd.read_csv(r'C:\Users\acastaneda\Downloads\casos_bonos.csv',sep=';',nrows= 2,encoding = "ISO-8859-1",low_memory=False)
    #df_bono = pd.read_csv(r'C:\Users\acastaneda\Downloads\casos_bonos.csv',sep=';',encoding = "ISO-8859-1",low_memory=False)
    df_bono = pd.read_excel(
        r'G:\Mi unidad\Casos\Casos_Bono600\todos_casos_Bono 600_01042021-01042021.xlsx',
        sheet_name = 'Sheet1',
        nrows= 1,
        skiprows = 4,
        usecols = 'A:AL')
    bono = df_bono.fillna(' ')
    print(bono)
    #Oracle
    cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_10")
    # sql = ('insert into CASOS_BONOS(ID,TICKET,DNI,CELULAR,CORREO,CASO,NOMBRE_BONO) '
    #     'values(:ID,:TICKET,:DNI,:CELULAR,:CORREO,:CASO,:NOMBRE_BONO)')
    # sql = ('insert into CASOS_BONOS(ID,TICKET,DNI,CELULAR,CORREO,CASO,NOMBRE_BONO) '
    #     'values(:ID,:TICKET,:DNI,:CELULAR,:CORREO,:CASO,:NOMBRE_BONO)')
    # sql = """insert into CASOS_BONOS(
    #         ID,
    #         TICKET,
    #         DNI,
    #         CELULAR,
    #         CORREO
    #     )
    #     values(
    #         :01,
    #         :TICKET,
    #         :DNI,
    #         :CELULAR,
    #         :CORREO
    #     )"""
    sql = config.sql
    # sql = ('insert into CASOS_BONOS(TICKET,DNI,CELULAR,CORREO,CASO,NOMBRE_BONO) '
    #     'values(:TICKET,:DNI,:CELULAR,:CORREO,:CASO,:NOMBRE_BONO)')
    connection = cx_Oracle.connect(
            config.username,
            config.password,
            config.dsn,
            encoding=config.encoding)
    # create a cursor
    cursor = connection.cursor()

    #Insert
    for index, row in bono.iterrows():
        #tabla_consolidada= [977985,row['TICKET'],row['DNI'],row['CELULAR'],row['CORREO']]
        tabla_consolidada = [
            977985,
            row['TICKET'],
            row['DNI'],
            row['CELULAR'],
            row['CORREO'],
            row['CASO'],
            'Bono 600',
            row['FECHA DE REGISTO'],
            row['DEPARTAMENTO'],
            row['ID'],
            row['APELLIDO PATERNO'],
            row['APELLIDO MATERNO'],
            row['NOMBRES'],
            row['BENEFICIARIO'],
            row['PROVINCIA'],
            row['DISTRITO'],
            row['LUGAR'],
            row['UBIGEO'],
            row['BANCO'],
            row['DNI CONTACTO'],
            row['APELLIDO PATERNO CONTACTO'],
            row['APELLIDO MATERNO CONTACTO'],
            row['NOMBRES CONTACTO'],
            row['CELULAR CONTACTO'],
            row['CORREO CONTACTO'],
            row['DEPARTAMENTO PERCEPTOR'],
            row['PROVINCIA PERCEPTOR'],
            row['DISTRITO PERCEPTOR'],
            row['UBIGEO PERCEPTOR'],
            row['CONSULTA'],
            row['REGISTRADOR'],
            row['ESTADO'],
            row['TIPO DE ATENCION'],
            row['EVALUADOR'],
            row['FECHA DE EVALUACION'],
            row['RESOLUCION DEL CASO'],
            row['CONCLUSIONES'],
            row['TIPO BONO'],
            row['CODIGO ENTIDAD']
        ]
        #cursor.execute(sql, [row['ID'], row['TICKET'],row['DNI'],row['CELULAR'],row['CORREO'],row['CASO'],row['NOMBRE_BONO']])
        cursor.execute(sql,tabla_consolidada)
        connection.commit()
        print(f"Actualizado item: {row['ID']} hora {datetime.now()}")
    connection.close()