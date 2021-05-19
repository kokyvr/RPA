#Librerias Python
import traceback
from datetime import date
from datetime import timedelta
from pathlib import Path

#Librerias Propias
from .datos_bono import datos_bono
from .descargar_adjunto import descargar_adjunto


def consolidar_descargar_adjuntos(dias_anteriores,repeticiones):
    print('='*80)
    lst_bono = ['Bono 600','Bono BFU']

    try:
        for tipo_bono in lst_bono:
            descargar_adjunto(tipo_bono,dias_anteriores,repeticiones)
            
    except Exception as e:
        print(f"Existe un error: {traceback.format_exc()}")
    
    print('='*80)
