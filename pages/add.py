import streamlit as st
import datetime
import pandas as pd
import sql_manager as sm

st.set_page_config(
    page_title="NCSC Form",
    page_icon="📝",
    layout="wide",
)

conn = sm.make_connection("mysql", "sql")
st.logo(image="./images/NCSC.png")
st.page_link("main.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)

with st.form("senior_form"):
    st.write("### Senior Citizen Form")

    with st.expander("Personal Information", expanded=True, icon="ℹ️"):
        name = st.text_input("Full Name")
        address = st.text_input("Address")

        col1, col2 = st.columns(2)
        with col1:
            birthdate = st.date_input(
                "Birthdate",
                value=None,
                format="YYYY-MM-DD",
                min_value=datetime.date(1900, 1, 1),
                max_value=datetime.date.today()
                - datetime.timedelta(days=60 * 365.25),
            )
        with col2:
            birthplace = st.text_input("Birthplace")

        col1, col2, col3 = st.columns(3)
        with col1:
            status = st.selectbox(
                "Status", ["Single", "Married", "Separated", "Widowed"], index=None
            )
        with col2:
            sex = st.selectbox("Sex", ["Male", "Female"], index=None)
        with col3:
            blood_type = st.selectbox(
                "Blood Type",
                ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
                index=None,
            )

        religion = st.text_input("Religion")
        # troll
        # contact_number = st.slider("Contact Number", min_value=9000000000, max_value=9999999999, step=1)
        col1, col2 = st.columns(2)
        with col1:
            contact_number = st.text_input("Primary Contact Number")
            father = st.text_input("Father's Name")
        with col2:
            email = st.text_input("Email Address")
            mother = st.text_input("Mother's Name")

        spouse = st.text_input("Spouse Name")

    with st.expander("Children or Dependent Information", expanded=True, icon="👪"):
        dependent_df = st.data_editor(
            data=pd.DataFrame(columns=["Name", "Is Child", "Is Working", "Occupation", "Income", "Birthdate"]),
            column_config={
                "Name": st.column_config.TextColumn("Name", required=True),
                "Is Child": st.column_config.CheckboxColumn("Is a children of the SC?", required=True),
                "Is Working": st.column_config.CheckboxColumn("Is currently working?", required=True),
                "Occupation": st.column_config.TextColumn("Occupation"),
                "Income": st.column_config.NumberColumn("Income", min_value=0),
                "Birthdate": st.column_config.DateColumn("Birthdate", 
                                                         format="YYYY-MM-DD",
                                                         min_value=datetime.date(1900, 1, 1),
                                                         max_value=datetime.date.today()),
            },
            num_rows="dynamic",
            use_container_width=True,
        )

    with st.expander("Income Information", expanded=True, icon="🪙"):
        income_df = st.data_editor(
            data=pd.DataFrame(columns=["Source", "Occupation", "Amount"]),
            column_config={
                "Source": st.column_config.SelectboxColumn("Source", options=["Salary", "Pension", "Business", "Insurance", "Savings", "Stocks"], required=True), 
                "Occupation": st.column_config.TextColumn("Occupation"),
                "Amount": st.column_config.NumberColumn("Amount", min_value=0, required=True),
            },
            num_rows="dynamic",
            use_container_width=True,
        )

    with st.expander("Health Concerns", expanded=True, icon="🩺"):
        concern_df = st.data_editor(
            data=pd.DataFrame(columns=["Type", "Details"]),
            column_config={
                "Type": st.column_config.SelectboxColumn("Type", options=["Medical", "Dental", "Optical", "Hearing", "Social"], required=True),
                "Details": st.column_config.TextColumn("Details", required=True),
            },
            num_rows="dynamic",
            use_container_width=True,
        )

    with st.expander("Educational Information", expanded=True, icon="🎓"):
        schools_df = sm.get_schools(conn)
        schools = schools_df["SchoolName"].to_list()
        education_df = st.data_editor(
            data=pd.DataFrame(columns=["Level", "School Name"]),
            column_config={
                "Level": st.column_config.SelectboxColumn("Level", options=["Primary", "Secondary", "Tertiary"], required=True),
                "School Name": st.column_config.SelectboxColumn("School Name", options=schools,required=True),
            },
            num_rows="dynamic",
            use_container_width=True,
        )

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Submitted!")