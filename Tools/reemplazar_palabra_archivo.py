#Librerias Python
import os
import traceback
from datetime import date
from datetime import timedelta

def reemplazar_palabra_archivo(archivo_inicial,archivo_final,palabra_inicial,palabra_final):
    #read input file
    fin = open(archivo_inicial, "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    for index,item in enumerate(palabra_inicial):
        data = data.replace(item,palabra_final[index])
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open(archivo_final, "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()