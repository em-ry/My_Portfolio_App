from dotenv import load_dotenv
import os
import smtplib, ssl

load_dotenv()

EMAIL_ADDR = ""
EMAIL_PWD = ""


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    password = os.getenv("EMAIL_PWD")
    username = os.getenv("EMAIL_ADDR")

    # create receiver address
    receiver = os.getenv("EMAIL_ADDR")
    # create secure context
    context = ssl.create_default_context()

    # create server
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
