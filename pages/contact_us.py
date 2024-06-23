import streamlit as st


st.subheader("Contact Me")

with st.form(key="Email_form"):
    user_email= st.text_input("Your email address")
    message= st.text_area("Your Message")
    button= st.form_submit_button()
    if button:
        message= message + user_email
        print("i was pressed")