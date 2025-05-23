import smtplib
import ssl
import streamlit as st


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    password = st.secrets["EMAIL_PWD"]
    username = st.secrets["EMAIL_ADDR"]

    # create receiver address
    receiver = st.secrets["EMAIL_ADDR"]
    # create secure context
    context = ssl.create_default_context()

    # create server
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
