import streamlit as st

# st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("pIC.jpg")


with col2:
    st.title("MMACHI EZEH")
    content = """
    Hi, i am Mmachi! i am a Python programmer,
    i started learning about tech in 2022, and i can say i am still improving,
    i am great at teamwork, and challenging my self, i love and work for growth"""
  
    st.info(content)

content1 = """ Below you can find some of the apps i have built in python. feel free to contact me!"""
st.write(content1)
