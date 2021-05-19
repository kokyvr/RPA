from email import message
import smtplib
from config import config
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# def enviar_mail_con_adjunto():
#     message = 'Hola Mundo'
#     subject = 'Prueba de Correo'
#     message = 'Subject: {} \n\n {}'.format(subject,message)
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.starttls()
#     server.login(config.mail_user,config.mail_pass)
#     server.sendmail(config.mail_user,config.mail_user,message)
#     server.quit()

def enviar_mail_con_adjunto(asunto,contenido,emails,file):
    message = MIMEMultipart('plain')
    message['From']= config.mail_user
    message['To']= ', '.join( emails ) 
    message['Subject']= asunto
    mail_content = contenido
    message.attach(MIMEText(mail_content, 'plain'))
    file = file +'.xlsx'
    attach_file_name = r'G:\Mi unidad\Casos\Reportes\{}'.format(file)
    attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment
    #add payload header with filename
    payload.add_header('Content-Disposition', 'attachment', filename=file)
    message.attach(payload)
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(config.mail_user, config.mail_pass) #login with mail_id and password
    session.sendmail(config.mail_user, emails, message.as_string())
    session.quit()
    print('Mail Enviando')