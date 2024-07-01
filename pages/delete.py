import streamlit as st
import sql_manager as sm
import pandas as pd

st.set_page_config(
    page_title="Deletion Confirmation",
    page_icon="🗑️",
    layout="wide",
)

st.warning("This section can only delete from the 'Senior' table as of now.", icon="⚠️")

conn = sm.make_connection()
st.logo(image="./images/NCSC.png")
st.page_link("main.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)

st.write(st.session_state.table_pk)
st.write(st.session_state.referencecode)

if st.session_state.selected_table == "Senior":
    df = pd.read_sql_query(f"SELECT * FROM senior WHERE referencecode = {st.session_state.referencecode};", conn)
    st.dataframe(df, hide_index=True, use_container_width=True)

    st.write("Are you sure you want to delete this record?")
        
    del_btn = st.button("Yes, delete")
    if del_btn:
        sm.delete_senior(st.session_state.referencecode)
        st.success("Record deleted successfully!")