import cx_Oracle
import pandas as pd
import config as cfg
from datetime import datetime


def insert_into_many(bono):
    """
    insert multiple billings
    :param billings: a list of billings
    :return:
    """
    cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_10")
    # construct an insert statement that add a new row to the billing_headers table
    sql = ('insert into CASOS_BONOS(ID,TICKET,DNI,CELULAR,CORREO,CASO,NOMBRE_BONO) '
        'values(:ID,:TICKET,:DNI,:CELULAR,:CORREO,:CASO,:NOMBRE_BONO)')

    try:
        # establish a new connection
        with cx_Oracle.connect(cfg.username,
                            cfg.password,
                            cfg.dsn,
                            encoding=cfg.encoding) as connection:
            # create a cursor
            with connection.cursor() as cursor:
                # execute the insert statement
                cursor.executemany(sql, bono)
                # commit work
                connection.commit()
        print("Procesado con éxito")
    except cx_Oracle.Error as error:
        print('Error occurred:')
        print(error)


if __name__ == '__main__':
    bono = pd.read_csv(r'C:\Users\acastaneda\Downloads\casos_bonos.csv',sep=';',nrows= 200,encoding = "ISO-8859-1")
    dataToInsert=[tuple(row) for row in bono.values]
    print(dataToInsert)
    # bono = [
    #     (datetime.now(),1000, 1, None),
    #     (datetime.now(), 1500, 2, None),
    #     (datetime.now(), 1700, 3, None),
    # ]
    # insert multiple billings
    insert_into_many(dataToInsert)