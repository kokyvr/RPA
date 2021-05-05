#Librerias Python
import traceback
from datetime import date
from datetime import timedelta
from pathlib import Path

#Librerias Propias
from .datos_bono import datos_bono
from .descargar_casos import descargar_casos


def consolidar_descargar_casos(dias_anteriores,repeticiones,caso = 'todos'):
    print('='*80)
    lst_bono = ['Bono 600','Bono BFU','Bono RURAL','Bono URBANO']

    try:
        for tipo_bono in lst_bono:
            descargar_casos(tipo_bono,dias_anteriores,repeticiones,caso)
            
    except Exception as e:
        print(f"Existe un error: {traceback.format_exc()}, tipo de casos:{caso}")
    
    print('='*80)


