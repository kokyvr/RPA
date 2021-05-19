#Librerias Python
import traceback
from datetime import date
from datetime import timedelta
from pathlib import Path

#Librerias Propias
from .importar_mensajes import importar_mensajes



def consolidar_importar_mensajes():
    print('='*80)
    lst_bono = ['Bono 600',]
    

    try:
        for tipo_bono in lst_bono:
            importar_mensajes(tipo_bono)
            
    except Exception as e:
        print(f"Existe un error: {traceback.format_exc()}")
    
    print('='*80)


