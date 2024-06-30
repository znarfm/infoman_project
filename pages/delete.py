import streamlit as st
from streamlit_free_text_select import st_free_text_select
import datetime
import sql_manager as sm

st.set_page_config(
    page_title="National Commission of Senior Citizens",
    page_icon="🏠",
    layout="wide",
    # initial_sidebar_state="collapsed",
)

conn = sm.make_connection("mysql", "sql")
# st.image("./images/NCSC.png", width=100)
st.page_link("main.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)