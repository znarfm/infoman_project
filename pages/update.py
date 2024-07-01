import streamlit as st
import datetime
import sql_manager as sm

st.set_page_config(
    page_title="Update Record",
    page_icon="✍️",
    layout="wide",
)

st.sidebar.warning("Application is still under development.", icon="⚠️")

conn = sm.make_connection()
st.logo(image="./images/NCSC.png")
st.page_link("main.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)

st.write(st.session_state.table_pk)
st.write(st.session_state.referencecode)