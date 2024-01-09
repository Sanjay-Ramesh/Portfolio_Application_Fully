import streamlit as st 

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images (2)\\photo.png")

with col2:
    st.title("Ardit Sluce")
    content = """Thala vanakkam ellarum eppidi irukingae. Idhu thaa mass tappa tappa hello inss.."""
    st.info(content)