import streamlit as st

st.header("Contact Me")

with st.form(key="email_forum"):
    user_email = st.text_input("Your Email Address")
    message = st.text_area("Your Messsage")
    button = st.form_submit_button()
    if button:
        message = message + user_email