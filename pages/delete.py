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

# st.write(st.session_state.table_pk)
# st.write(st.session_state.referencecode)

tables_dict = {"Senior":"senior", "Education":"education", "Health Concern":"healthconcern", "Income":"income", "Dependent":"dependent", "School":"school"}

if st.session_state.selected_table == "Senior":
    for k, v in tables_dict.items():
        if k == "School":
            continue
        st.markdown(f"### {k} Table")
        df = pd.read_sql_query(f"SELECT * FROM {v} WHERE referencecode = {st.session_state.referencecode};", conn)
        if k == "Senior":
            senior_name = df['Name'].iloc[0] 
            df.iloc[:, 0] = df.iloc[:, 0].astype(str)
        else:
            df.iloc[:, :2] = df.iloc[:, :2].astype(str)
        st.dataframe(df, hide_index=True, use_container_width=True)

    st.write(f"Are you sure you want to delete all related records of **{senior_name}**?")
    del_btn = st.button("Yes, delete.", type="primary")
    if del_btn:
        sm.delete_senior(st.session_state.referencecode)
        st.warning("All related records deleted successfully!", icon="🗑️")
        st.divider()
        st.page_link("main.py", label="Back to Home", icon="🏠")
else:
    table = tables_dict.get(st.session_state.selected_table)
    pk = st.session_state.table_pk
    table_pk_mapping = {
        "dependent": "DepID",
        "education": "EducID",
        "income": "IncomeID",
        "healthconcern": "ConcernID",
        "school": "SchoolID"
    }

    col_name_pk = table_pk_mapping.get(table)
    df = pd.read_sql_query(f"SELECT * FROM {table} WHERE {col_name_pk} = {pk};", conn)
    if table == "school":
        df.iloc[:, 0] = df.iloc[:, 0].astype(str)
    else:
        df.iloc[:, 1] = df.iloc[:, 1].astype(str)
    st.dataframe(df, hide_index=True, use_container_width=True)
    
    st.write(f"Are you sure you want to delete this record from **{st.session_state.selected_table}** table?")
    
    del_btn = st.button("Yes, delete", type="primary")
    if del_btn and not df.empty:
        sm.delete_record(table, pk)
        st.warning("Record deleted successfully!", icon="🗑️")
        st.divider()
        st.page_link("main.py", label="Back to Home", icon="🏠")