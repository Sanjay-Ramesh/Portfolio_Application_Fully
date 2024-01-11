import streamlit as st 
import pandas

st.set_page_config(layout="wide")

col1, col2  = st.columns(2)

with col1:
    st.image("images (2)\\photo.png")

with col2:
    st.title("Ardit Sluce")
    content = """Thala vanakkam ellarum eppidi irukingae. Idhu thaa mass tappa tappa hello inss.."""
    st.info(content)

content1 = """Below you can find some of the apps I have built in Python. Feel free to contact me. Vannakam ippo thala ma """
st.write(content1)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data (2).csv", sep=";")


with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images (2)\\"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images (2)\\"+row["image"])
        st.write(f"[Source Code]({row['url']})")



