import streamlit as st
import sql_manager as sm
import pandas as pd

st.set_page_config(
    page_title="Deletion Confirmation",
    page_icon="🗑️",
    layout="wide",
)

conn = sm.make_connection()
st.logo(image="./images/NCSC.png")
st.page_link("main.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)

st.warning("Section needs testing.", icon="🧪")

# st.write(st.session_state.table_pk)
# st.write(st.session_state.referencecode)

tables = ["senior", "education", "healthconcern", "income", "dependent"]

if st.session_state.selected_table == "Senior":
    for table in tables:
        df = pd.read_sql_query(f"SELECT * FROM {table} WHERE referencecode = {st.session_state.referencecode};", conn)
        st.dataframe(df, hide_index=True, use_container_width=True)

    st.write("Are you sure you want to delete this record and its related records?")
    del_btn = st.button("Yes, delete")
    if del_btn:
        sm.delete_senior(st.session_state.referencecode)
        st.success("Record deleted successfully!")
else:
    table = st.session_state.selected_table.lower()
    pk = st.session_state.table_pk

    df = pd.read_sql_query(f"SELECT * FROM {table} WHERE id = {pk};", conn)
    st.dataframe(df, hide_index=True, use_container_width=True)
    
    st.write(f"Are you sure you want to delete this record from {table}?")
    
    del_btn = st.button("Yes, delete")
    if del_btn:
        sm.delete_record(table, pk)
        st.success("Record deleted successfully!")