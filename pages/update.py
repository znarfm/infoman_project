import streamlit as st
import datetime
import sql_manager as sm
import pandas as pd

st.set_page_config(
    page_title="Update Record",
    page_icon="✍️",
    layout="wide",
)

st.warning("Section needs testing.", icon="🧪")

conn = sm.make_connection()
st.logo(image="./images/NCSC.png")
st.page_link("main.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)

table_selected = st.session_state.selected_table

if table_selected == "Senior":
    st.markdown(f"### {table_selected} Table")
    df = pd.read_sql_query(f"SELECT * FROM {table_selected} WHERE referencecode = {st.session_state.referencecode};", conn)
    df_to_edit = df.drop(columns=['ReferenceCode'])
    edited_df = st.data_editor(df_to_edit, hide_index=True, use_container_width=True)
    upd_btn = st.button("UPDATE")
    if upd_btn:
        table = st.session_state.selected_table.lower()
        
        try:
            sm.update_senior(table, edited_df, st.session_state.referencecode, "referencecode")
            st.success("Record updated successfully!")
        except Exception as e:
            st.error(f"Error updating record: {e}")
elif table_selected == "Education":
    st.markdown(f"### {table_selected} Table")
    df = pd.read_sql_query(f"SELECT * FROM {table_selected} WHERE referencecode = {st.session_state.referencecode};", conn)
    df_id = pd.read_sql_query(f"SELECT EducID FROM {table_selected} WHERE referencecode = {st.session_state.referencecode};", conn)
    df_to_edit = df.drop(columns=['EducID','ReferenceCode'])
    edited_df = st.data_editor(df_to_edit, hide_index=True, use_container_width=True)
    upd_btn = st.button("UPDATE")
    if upd_btn:
        table = st.session_state.selected_table.lower()
        
        for index, row in edited_df.iterrows():
            try:
                specific_value = df.iloc[index]['EducID']
                sm.update_record(table, row, specific_value, "EducID")
                st.success(f"Record {index + 1} updated successfully!")
            except Exception as e:
                st.error(f"Error updating record {index}: {e}")
elif table_selected == "Health Concern":
    st.markdown(f"### {table_selected} Table")
    df = pd.read_sql_query(f"SELECT * FROM healthconcern WHERE referencecode = {st.session_state.referencecode};", conn)
    df_id = pd.read_sql_query(f"SELECT ConcernID FROM healthconcern WHERE referencecode = {st.session_state.referencecode};", conn)
    df_to_edit = df.drop(columns=['ConcernID','ReferenceCode'])
    edited_df = st.data_editor(df_to_edit, hide_index=True, use_container_width=True)
    upd_btn = st.button("UPDATE")
    if upd_btn:
        table = "healthconcern"
        
        for index, row in edited_df.iterrows():
            try:
                specific_value = df.iloc[index]['ConcernID']
                sm.update_record(table, row, specific_value, "ConcernID")
                st.success(f"Record {index + 1} updated successfully!")
            except Exception as e:
                st.error(f"Error updating record {index}: {e}")
elif table_selected == "Income":
    st.markdown(f"### {table_selected} Table")
    df = pd.read_sql_query(f"SELECT * FROM {table_selected} WHERE referencecode = {st.session_state.referencecode};", conn)
    df_id = pd.read_sql_query(f"SELECT IncomeID FROM {table_selected} WHERE referencecode = {st.session_state.referencecode};", conn)
    df_to_edit = df.drop(columns=['IncomeID','ReferenceCode'])
    edited_df = st.data_editor(df_to_edit, hide_index=True, use_container_width=True)
    upd_btn = st.button("UPDATE")
    if upd_btn:
        table = st.session_state.selected_table.lower()
        
        for index, row in edited_df.iterrows():
            try:
                specific_value = df.iloc[index]['IncomeID']
                sm.update_record(table, row, specific_value, "IncomeID")
                st.success(f"Record {index + 1} updated successfully!")
            except Exception as e:
                st.error(f"Error updating record {index}: {e}")
elif table_selected == "Dependent":
    st.markdown(f"### {table_selected} Table")
    df = pd.read_sql_query(f"SELECT * FROM {table_selected} WHERE referencecode = {st.session_state.referencecode};", conn)
    df_id = pd.read_sql_query(f"SELECT DepID FROM {table_selected} WHERE referencecode = {st.session_state.referencecode};", conn)
    df_to_edit = df.drop(columns=['DepID','ReferenceCode'])
    edited_df = st.data_editor(df_to_edit, hide_index=True, use_container_width=True)
    upd_btn = st.button("UPDATE")
    if upd_btn:
        table = st.session_state.selected_table.lower()
        
        for index, row in edited_df.iterrows():
            try:
                specific_value = df.iloc[index]['DepID']
                sm.update_record(table, row, specific_value, "DepID")
                st.success(f"Record {index + 1} updated successfully!")
            except Exception as e:
                st.error(f"Error updating record {index}: {e}")
elif table_selected == "School":
    st.markdown(f"### {table_selected} Table")
    df = pd.read_sql_query(f"SELECT * FROM {table_selected} WHERE SchoolID = {st.session_state.referencecode};", conn)
    df_to_edit = df.drop(columns=['SchoolID'])
    edited_df = st.data_editor(df_to_edit, hide_index=True, use_container_width=True)
    upd_btn = st.button("UPDATE")
    if upd_btn:
        table = st.session_state.selected_table.lower()
        
        try:
            sm.update_senior(table, edited_df, st.session_state.referencecode, "SchoolID")
            st.success("Record updated successfully!")
        except Exception as e:
            st.error(f"Error updating record: {e}")