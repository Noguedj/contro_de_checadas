#!/usr/bin/python
import subprocess, time
hosts = ("8.8.8.8", "yahoo.com")
def ping(host):
    ret = subprocess.call(["ping", "-c", "3", "-w", "5", host],stdout = open("/dev/null", "w"), stderr = open("/dev/null", "w"))
    return ret == 0
print ("checando red")
xstatus = 1
if ping("8.8.8.8"):
    q = "true"
    xstatus = 0
if xstatus:
    q = "false"
    import os
    os.system("python /home/pi/Downloads/reloj.py")
    
if q == "true":
#Fin de la prueba
#enviar correo
    import smtplib
    import time
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    date = time.strftime("%y-%m-%d")
    times = time.strftime("%H:%M:%S")
    email_user = "sistemas@novalinkmx.com"
    email_send = "sistemas@novalinkmx.com"
    subject = "Checador de Transporte 01 "
    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["To"] = email_send
    msg["Subject"] = subject
    body = " Fecha: " + date + "  " + " Hora: " + times
    msg.attach(MIMEText(body,"plain"))
    filename = "FF_21.txt"
    attachment = open(filename, "rb")
    part = MIMEBase("application", "aoctet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("content-disposition", "attachment; filename = " + filename)
    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email_user,"*nova!123")
    server.sendmail(email_user, email_send, text)
    server.quit()
#fin del envio

        
        
            
            
            
    
