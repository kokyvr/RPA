import cx_Oracle
import config

connection = None
try:
    cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_10")
    connection = cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding=config.encoding)

    # show the version of the Oracle Database
    print(connection.version)
except cx_Oracle.Error as error:
    print(error)
finally:
    # release the connection
    if connection:  
        connection.close()

