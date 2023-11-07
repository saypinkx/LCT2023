import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'otherstest@yandex.ru'
EMAIL_HOST_PASSWORD = 'vjyamowogvxfktbi'
EMAIL_PORT = 465


def send_mail(subject, text, recipient_email):
    message = MIMEMultipart()
    message['From'] = EMAIL_HOST_USER
    message['To'] = recipient_email
    message['Subject'] = subject
    body = MIMEText(text)
    message.attach(body)
    with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as server:
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.send_message(message)
