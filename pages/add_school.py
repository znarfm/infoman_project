import streamlit as st
import datetime
import pandas as pd
import sql_manager as sm

st.set_page_config(
    page_title="School Records",
    page_icon="🎓",
    layout="wide",
)

st.sidebar.warning("Section under development.", icon="⚠️")

conn = sm.make_connection("mysql", "sql")
st.logo(image="./images/NCSC.png")
st.page_link("main.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)

