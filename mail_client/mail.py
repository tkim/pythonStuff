import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# setup gmail for smtp
# gmail smtp port (TLS) 587
# SMTP port(SSL) 465

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    # encrypt the line
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Grab dinner this weekend?'
    body = 'How about dinner at 6pm this saturday.'

    msg = f'Subject: {subject}\n\n{body}'

    # smtp.sendmail(SENDER, RECIEVER, msg)
    smtp.sendmail(EMAIL_ADDRESS, terrence.kim@gmail.com, msg)








