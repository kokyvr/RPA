#Librerias Python
import traceback
from datetime import date
from datetime import timedelta
#Librerias Propias
from applications.bono.apps.actualizar_bd import actualizar_db

def realizar_iteraciones(dias_anteriores, repeticiones):
        
        for i in range(dias_anteriores):
            #Variables
            var_fecha =date.today() - timedelta(days=dias_anteriores-i)
            var_date = var_fecha.strftime('%Y-%m-%d')
            try:
                print(f'Iniciando operación para la fecha: {var_date}')
                actualizar_db(var_date)
            except Exception as e:
                print(f"Existe un error : {traceback.format_exc()}")
            
            #Termino de repeticiones
            if i == repeticiones - 1:
                    break