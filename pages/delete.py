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

tables_dict = {"Senior":"senior", "Education":"education", "Health Concern":"healthconcern", "Income":"income", "Dependent":"dependent"}

if st.session_state.selected_table == "Senior":
    for k, v in tables_dict.items():
        st.markdown(f"### {k} Table")
        df = pd.read_sql_query(f"SELECT * FROM {v} WHERE referencecode = {st.session_state.referencecode};", conn)
        st.dataframe(df, hide_index=True, use_container_width=True)
        if k == "Senior":
            senior_name = df['Name'].iloc[0] 

    st.write(f"Are you sure you want to delete all related records of {senior_name}?")
    del_btn = st.button("Yes, delete.")
    if del_btn:
        sm.delete_senior(st.session_state.referencecode)
        st.toast(f"All related records of {senior_name} deleted successfully!", icon="🗑️")
        st.divider()
        st.page_link("main.py", label="Back to Home", icon="🏠")
else:
    table = st.session_state.selected_table.lower()
    pk = st.session_state.table_pk
    table_pk_mapping = {
        "dependent": "DepID",
        "education": "EducID",
        "income": "IncomeID",
        "healthconcern": "ConcernID",
        "school": "SchoolID"
    }

    col_name = table_pk_mapping.get(table)
    df = pd.read_sql_query(f"SELECT * FROM {table} WHERE {col_name} = {pk};", conn)
    st.dataframe(df, hide_index=True, use_container_width=True)
    
    st.write(f"Are you sure you want to delete this record from {table}?")
    
    del_btn = st.button("Yes, delete")
    if del_btn:
        sm.delete_record(table, pk)
        st.toast("Selected {table} Record deleted successfully!", icon="🗑️")
        st.divider()
        st.page_link("main.py", label="Back to Home", icon="🏠")