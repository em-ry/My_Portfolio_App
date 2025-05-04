import pandas
import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/emrypydev.png")

with col2:
    st.title("EmryPythonDev")
    content = """ 
    Hey there! I’m Emry, a python developer on a journey  to master Python 
    and break into the world of Web3 and blockchain development using technologies like Cartesi.
    I currently build Python-powered tools and web apps that solve simple, real-world problems — 
    like automating tasks, scraping data, and creating clean, functional interfaces.
    
    This portfolio is a growing log of my progress—one project at a time. Thanks for stopping by!
    """
    st.info(content)

text_line = "Below you can find some of the apps i have built in python. Feel free to contact me!"
st.write(text_line)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("new_data.csv")

with col3:
    for index, item in df[:10].iterrows():
        st.header(item["title"])
        st.write(item["description"])
        st.image("images/" + item["image"])
        st.write(f"[Source code]({item['url']})")

with col4:
    for index, item in df[10:].iterrows():
        st.header(item["title"])
        st.write(item["description"])
        st.image("images/" + item["image"])
        st.write(f"[Source code]({item['url']})")
