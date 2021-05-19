#Librerias Python
import traceback
from datetime import date
from datetime import timedelta
#Librerias Propias
from applications.bono.apps.actualizar_bd import actualizar_db
from tools.ejecutar_query_desde_excel import ejecutar_query_desde_excel

def registrar_original_bd():
    var_fecha =date.today() - timedelta(days=1)
    var_date = var_fecha.strftime('%Y-%m-%d')
    try:
        print(f'Iniciando operación para la fecha: {var_date}')
        ejecutar_query_desde_excel(var_date,'query_original','A:J')
    except Exception as e:
        print(f"Existe un error : {traceback.format_exc()}")
            
