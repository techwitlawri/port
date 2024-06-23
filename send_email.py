import smtplib, ssl
# smtplib is an email libary
# ssl is to send email safely
host= "smtp.gmail.com"
port= 465

username= "mmachilawri@gmail.com"
password= "bqlj nmdu dhmj hfjr"

receiver= "mmachilawri@gmail.com"
context= ssl.create_default_context()
message= """ \
Subject : Hi
 Hi,
how are you?"""

with smtplib.SMTP_SSL(host, port, context= context) as  server:
    server.login(username, password)
    server.sendmail(username, receiver, message)