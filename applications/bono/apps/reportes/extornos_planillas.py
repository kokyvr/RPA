#Librerias Python
import os
from datetime import date
from datetime import timedelta
#Librerias Propias
from tools.mail.enviar_mail_con_adjunto import enviar_mail_con_adjunto
from tools.oracle.reporte_desde_query import reporte_desde_query

def extornos():
    #Variables Extornos
    var_fecha =date.today() - timedelta(days=1)
    var_fecha_hoy = var_fecha.strftime('%Y-%m-%d')
    sql_extornos="""select * from USER_APOYO1.CASOS_BONOS
    where nombre_bono = '600' and FECHA_REGISTRO LIKE '{}%' AND ESTADO_SOLICITUD_ORIGINAL = 'Válida' AND CODIGO_CASOS = 'CP'
    and PLANILLA_ORIGINAL ='PLANILLA CON RD' """.format(var_fecha_hoy)
    file = f'{var_fecha_hoy} - Extornos'
    asunto = f'{var_fecha_hoy} - Reporte de Casos para realizar Extornos'
    emails = ['contratista02@pension65.gob.pe','alxcasta13@gmail.com','mpazsoldan@pension65.gob.pe']
    var_registro=reporte_desde_query(sql_extornos,file)
    contenido = f"""
        Buenos Días soy el Robot
        Se remite el correo del Reporte de Casos para realizar Extornos de la fecha - {var_fecha_hoy}.
        Teniendo {var_registro} registros.
        Saludos"""
    enviar_mail_con_adjunto(asunto,contenido,emails,file)


def planillas():
    #Variables Planillas
    var_fecha =date.today() - timedelta(days=1)
    var_fecha_hoy = var_fecha.strftime('%Y-%m-%d')
    sql_extornos="""select * from USER_APOYO1.CASOS_BONOS
    where nombre_bono = '600' and FECHA_REGISTRO LIKE '{}%' AND ESTADO_SOLICITUD_ORIGINAL = 'Válida' AND CODIGO_CASOS = 'CP'
    and PLANILLA_ORIGINAL ='PLANILLA SIN RD' """.format(var_fecha_hoy)
    file = f'{var_fecha_hoy} - Planillas'
    asunto = f'{var_fecha_hoy} - Reporte de Casos para realizar Planillas'
    emails = ['contratista02@pension65.gob.pe','alxcasta13@gmail.com','mpazsoldan@pension65.gob.pe']
    var_registro=reporte_desde_query(sql_extornos,file)
    contenido = f"""
        Buenos Días soy el Robot
        Se remite el correo del Reporte de Casos para realizar Extornos de la fecha - {var_fecha_hoy}.
        Teniendo {var_registro} registros.
        Saludos"""
    enviar_mail_con_adjunto(asunto,contenido,emails,file)