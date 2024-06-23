import smtplib, ssl
# smtplib is an email libary
# ssl is to send email safely
import os


def send_email(message):
    host= "smtp.gmail.com"
    port= 465

    username= "mmachilawri@gmail.com"
    password=  os.getenv("PASSWORD")

    receiver= "mmachilawri@gmail.com"
    context= ssl.create_default_context()
    
    with smtplib.SMTP_SSL(host, port, context= context) as  server:
        server.login(username, password)
        server.sendmail(username, receiver, message)