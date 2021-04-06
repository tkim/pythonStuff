import smtplib
from email import encoder
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart 

# setup email login

# incoming mail imap.gmail.com Port 993 - requires SSL
# gmail smtp port (TLS) 587
# SMTP port(SSL) 465
server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('terrence.kim@gmail.com', password)

# message
msg = MIMEMultipart()
msg['From'] = 'Me'
msg['To'] = 'terrence.kim@gmail.com'
msg['Subject'] = "Just a test"

with open('message.txt, 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

# attach jpg
filename = 'coding.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read)

encoders.encode_base64(p)

p.add_header('Content-Disposition', f'attachement; filename={filename}')
msg.attach(p)

# send the message
text = msg.as_string()
server.sendmail('terrence.kim@gmail.com', 'terrence.kim@gmail.com', text)