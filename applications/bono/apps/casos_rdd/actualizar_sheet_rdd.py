#Libreias propias
from tools.oracle.df_desde_query import df_desde_query


def actualizar_sheet_rdd():
    query="""select * from USER_APOYO1.CASOS_BONOS TB
                where   
                nombre_bono = '600' and 
                (TO_NUMBER(ID_consulta)>=195089 and TO_NUMBER(ID_consulta)<=201007) and
                TIPO_CASOS!='Beneficiario no reconoce a perceptor del bono' and
                PERTENECE_MIDIS='SI' and
                CODIGO_CASOS = 'RD'"""
    df=df_desde_query(query)

    for index, row in df.iterrows():
        print(row['ID_CONSULTA'])