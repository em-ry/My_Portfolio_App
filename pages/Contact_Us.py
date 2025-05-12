from send_email import send_email
import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms", clear_on_submit=True):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from Portfolio App!

From: {user_email}
{raw_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Message sent!!")
