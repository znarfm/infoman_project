import streamlit as st
import pandas as pd
import sql_manager as sm

st.set_page_config(
    page_title="School Records",
    page_icon="🎓",
    layout="wide",
)

conn = sm.make_connection()
st.logo(image="./images/NCSC.png")
st.page_link("main.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)

existing_ids = pd.read_sql_query("SELECT SchoolID FROM school;", conn)

def add_school():
    with st.form("add_school"):
        school_id = st.text_input("School ID*")
        school_name = st.text_input("School Name*")
        school_address = st.text_input("School Address*")

        if st.form_submit_button("Add School"):
            if not (school_id or school_name or school_address):
                st.error("Please fill in all required fields.")
                return

            if not school_id.isnumeric():
                st.error("School ID must be a number.")
                return
                
            school_id = int(school_id)
            if school_id in existing_ids["SchoolID"].values:
                st.error(f"School ID {school_id} already exists.")
                return
            school_data = {"School ID": school_id, "School Name": school_name, "School Address": school_address}
            confirmation(school_data)

@st.experimental_dialog("Confirmation", width="large")
def confirmation(school_data: dict):
    school_data_df = pd.DataFrame(school_data, index=[0])
    st.dataframe(school_data_df, use_container_width=True, hide_index=True, 
                 column_config={
                     "School ID": st.column_config.TextColumn()})

    st.write("Are you sure you want to add this school?")
    confirm_btn = st.button("Yes, add school.")

    if confirm_btn:
        if sm.insert_school(school_data):
            st.success("School added successfully!")
            st.page_link("main.py", label="Back to Home", icon="🏠")


add_school()