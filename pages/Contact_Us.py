import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forum"):
    user_email = st.text_input("Your Email Address")
    row_message = st.text_area("Your Messsage")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{row_message}"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was Sent Successfully")