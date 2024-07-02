import streamlit as st
import datetime
import pandas as pd
import sql_manager as sm

st.set_page_config(
    page_title="Record Information",
    page_icon="🧓",
    layout="wide",
)

st.warning("This section is still under development.", icon="⚠️")

conn = sm.make_connection()
st.logo(image="./images/NCSC.png")
st.page_link("main.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)

table = st.session_state.selected_table
selected = st.session_state.referencecode
selected_df = pd.read_sql_query(f"SELECT * FROM {table} WHERE referencecode = '{selected}';", conn)
st.dataframe(selected_df, hide_index=True, use_container_width=True)

st.write(st.session_state.table_pk)
st.write(st.session_state.referencecode)