#Librerias Python
import traceback
#Librerias Python - Oracle
import cx_Oracle
#Librerias Python - Pandas
import pandas as pd

#Librerias Propias
from config import config
from .datos_bono import datos_bono

def insertar_casos(tipo_bono,inicio,fin, caso = 'todos'):
    print('-'*80)
    try:
        bono = datos_bono(tipo_bono)
        df_bono = pd.read_excel(
            r'{ruta_bono}\{caso}_casos_{tipo_bono}_{inicio}-{fin}.xlsx'.format(
                ruta_bono=bono['ruta_bono'],
                tipo_bono=bono['bono'],
                caso='todos',
                inicio=inicio,
                fin=fin,
                ),
            sheet_name = 'Sheet1',
            skiprows = 4,
            usecols = 'A:AL')
        
        bd_bono = df_bono.fillna(' ')

        #Oracle
        try:
            print('Oracle por Iniciar')
            cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_10")
        except:
            print('Oracle Iniciado')

        sql = config.sql

        connection = cx_Oracle.connect(
                config.username,
                config.password,
                config.dsn,
                encoding=config.encoding)
        # create a cursor
        cursor = connection.cursor()
        #Insert
        iteraciones = 0
        exito = 0
        error = 0
        tabla_error = []
        for index, row in bd_bono.iterrows():
            iteraciones += 1
            tb_valores= [
                row['TICKET'],
                row['DNI'],
                str(row['CELULAR']),
                str(row['CORREO']),
                str(row['CASO']),
                str(bono['sigla']),
                str(row['FECHA DE REGISTO']),
                str(row['DEPARTAMENTO']),
                row['ID'],
                str(row['APELLIDO PATERNO']),
                str(row['APELLIDO MATERNO']),
                str(row['NOMBRES']),
                str(row['BENEFICIARIO']),
                str(row['PROVINCIA']),
                str(row['DISTRITO']),
                str(row['LUGAR']),
                str(row['UBIGEO']),
                str(row['BANCO']),
                str(row['DNI CONTACTO']),
                str(row['APELLIDO PATERNO CONTACTO']),
                str(row['APELLIDO MATERNO CONTACTO']),
                str(row['NOMBRES CONTACTO']),
                str(row['CELULAR CONTACTO']),
                str(row['CORREO CONTACTO']),
                # row['DEPARTAMENTO PERCEPTOR'],
                # row['PROVINCIA PERCEPTOR'],
                # row['DISTRITO PERCEPTOR'],
                # row['UBIGEO PERCEPTOR'],
                str(row['CONSULTA']),
                str(row['REGISTRADOR']),
                str(row['ESTADO']),
                str(row['TIPO DE ATENCION']),
                str(row['EVALUADOR']),
                str(row['FECHA DE EVALUACION']),
                str(row['RESOLUCION DEL CASO']),
                str(row['CONCLUSIONES']),
                str(row['TIPO BONO']),
                # row['CODIGO ENTIDAD']
            ]
            try:
                cursor.execute(sql,tb_valores)
                connection.commit()
                #print(f"Actualizado item: {row['ID']} hora {datetime.now()}")
                exito += 1
            except:
                tabla_error.append(bd_bono.iloc[index])
                print(f'Error {traceback.format_exc()} in indice: {index}')
                error +=1
        
        #Guardando Archivo del Error
        df_error = pd.DataFrame(tabla_error)
        ruta_df_error = r'{ruta_bono}\{caso}_casos_{tipo_bono}_{inicio}-{fin}_error.csv'.format(
                ruta_bono=bono['ruta_bono'],
                tipo_bono=bono['bono'],
                caso='todos',
                inicio=inicio,
                fin=fin,
                )
        if len(df_error.index) > 0:
            df_error.to_csv(ruta_df_error,index = False, header=True)

        # Finalizando el comando
        print('==='*50)
        print('Resultado del Bono: {bono} en la fecha {date} se ha tenido exito: {exito} y error {error} de un total de {total}'.format(
            bono=bono['bono'],
            date=inicio,
            exito=exito,
            error=error,
            total=iteraciones
        ))
        print('==='*50)

        connection.close()

    except:
        print(f'Existe un error en el {tipo_bono}: {traceback.format_exc()}, tipo de casos:{caso}')
    print('-'*80)
