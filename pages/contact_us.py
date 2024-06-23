import streamlit as st
from send_email import send_email

st.subheader("Contact Me")

with st.form(key="Email_form"):
    user_email= st.text_input("Your email address")
    message= st.text_area("Your Message")
    raw_message= st.text_area("your message")
    message= f"""\
Subject : New email from{user_email}
From : {user_email}
{raw_message}
"""
    button= st.form_submit_button()
    if button:
        message= message + user_email
        send_email(message)
        st.info("your email was sent")