import streamlit as st
import datetime
import pandas as pd
import sql_manager as sm
import re

st.set_page_config(
    page_title="NCSC Form",
    page_icon="📝",
    layout="wide",
)

conn = sm.make_connection()
st.logo(image="./images/NCSC.png")
st.page_link("main.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)

def senior_form():
    with st.form("senior_form"):
        st.write("### Senior Citizen Form")
        st.info("All fields marked with * are required.", icon="ℹ️")

        with st.expander("Personal Information", expanded=True, icon="📒"):
            name = st.text_input("Full Name*").strip()
            address = st.text_input("Address*").strip()

            col1, col2 = st.columns(2)
            with col1:
                birthdate = st.date_input(
                    "Birthdate*",
                    value=None,
                    format="YYYY-MM-DD",
                    min_value=datetime.date(1900, 1, 1),
                    max_value=datetime.date.today()
                    - datetime.timedelta(days=60 * 365.25),
                )
            with col2:
                birthplace = st.text_input("Birthplace*").strip()

            col1, col2, col3 = st.columns(3)
            with col1:
                status = st.selectbox(
                    "Status*", options=["Single", "Married", "Separated", "Widowed"], index=None
                )
            with col2:
                sex = st.selectbox("Sex*", options=["Male", "Female"], index=None)
            with col3:
                blood_type = st.selectbox(
                    "Blood Type*",
                    ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "Unknown"],
                    index=None,
                )

            religion = st.selectbox("Religion*", options=['Roman Catholic', 'Islam', 'Iglesia ni Cristo', 'Jehovah\'s Witnesses', 'Evangelical', 'Baptist', 'Mormon', 'Buddhist', 'Hindu', 'Others'], index=None)
            # troll
            # contact_number = st.slider("Contact Number", min_value=9000000000, max_value=9999999999, step=1)
            col1, col2 = st.columns(2)
            with col1:
                contact_number = st.text_input("Contact Number").strip()
                father = st.text_input("Father's Name*").strip()
            with col2:
                email = st.text_input("Email Address").strip()
                mother = st.text_input("Mother's Name*").strip()

            spouse = st.text_input("Spouse Name")

        with st.expander("Children or Dependent Information", expanded=True, icon="👪"):
            dependent_df = pd.DataFrame(columns=["Name", "Is Child", "Is Working", "Occupation", "Income", "Birthdate"])
            dependent_df = st.data_editor(
                data=dependent_df,
                column_config={
                    "Name": st.column_config.TextColumn("Name", required=True),
                    "Is Child": st.column_config.CheckboxColumn("Is a children of the SC?", required=True, default=False),
                    "Is Working": st.column_config.CheckboxColumn("Is currently working?", required=True, default=False),
                    "Occupation": st.column_config.TextColumn("Occupation"),
                    "Income": st.column_config.NumberColumn("Income", min_value=0),
                    "Birthdate": st.column_config.DateColumn("Birthdate", 
                                                            format="YYYY-MM-DD",
                                                            min_value=datetime.date(1900, 1, 1),
                                                            max_value=datetime.date.today(),
                                                            required=True),
                },
                num_rows="dynamic",
                use_container_width=True,
            )

        with st.expander("Income Information", expanded=True, icon="🪙"):
            income_df = pd.DataFrame(columns=["Source", "Occupation", "Amount"])
            income_df = st.data_editor(
                data=income_df,
                column_config={
                    "Source": st.column_config.SelectboxColumn("Source", options=["Salary", "Pension", "Business", "Insurance", "Savings", "Stocks"], required=True), 
                    "Occupation": st.column_config.TextColumn("Occupation"),
                    "Amount": st.column_config.NumberColumn("Amount", min_value=0, required=True),
                },
                num_rows="dynamic",
                use_container_width=True,
            )

        with st.expander("Health Concerns", expanded=True, icon="🩺"):
            concern_df = pd.DataFrame(columns=["Type", "Details"])
            concern_df = st.data_editor(
                data=concern_df,
                column_config={
                    "Type": st.column_config.SelectboxColumn("Type", options=["Medical", "Dental", "Vision", "Hearing", "Social"], required=True),
                    "Details": st.column_config.TextColumn("Details", required=True),
                },
                num_rows="dynamic",
                use_container_width=True,
            )

        with st.expander("Educational Information", expanded=True, icon="🎓"):
            schools_df = pd.read_sql_query("SELECT SchoolID, SchoolName FROM school ORDER BY SchoolName", conn)
            schools = schools_df["SchoolName"].to_list()
            education_df = pd.DataFrame(columns=["Education Level", "School Name", "Year Started", "Year Completed"])
            education_df = st.data_editor(
                data=education_df,
                column_config={
                    "Education Level": st.column_config.SelectboxColumn("Level", options=["Primary", "Secondary", "Tertiary"], required=True),
                    "School Name": st.column_config.SelectboxColumn("School Name", options=schools,required=True),
                    "Year Started": st.column_config.NumberColumn("Year Started", format="%f", required=True,
                                                                min_value=1900, max_value=datetime.date.today().year),
                    "Year Completed": st.column_config.NumberColumn("Year Completed", format="%f", required=True,
                                                                min_value=1900, max_value=datetime.date.today().year),
                },
                num_rows="dynamic",
                use_container_width=True,
            )

        submitted = st.form_submit_button("Submit")
        if submitted:
            fields = {
                "Full Name": name,
                "Address": address,
                "Birthdate": birthdate,
                "Birthplace": birthplace,
                "Status": status,
                "Sex": sex,
                "Blood Type": blood_type,
                "Religion": religion,
                "Father's Name": father,
                "Mother's Name": mother
            }

            missing_fields = [field_name for field_name, field_value in fields.items() if not field_value]

            if missing_fields:
                st.error(f"Please fill in the following required fields: {', '.join(missing_fields)}")
            else:
                education_df["SchoolID"] = education_df["School Name"].apply(lambda x: schools_df[schools_df["SchoolName"] == x]["SchoolID"].values[0])
                summary = {
                "Personal Information": {
                    "Name": name,
                    "Address": address,
                    "Birthdate": birthdate,
                    "Birthplace": birthplace,
                    "Status": status,
                    "Sex": sex,
                    "Blood Type": blood_type,
                    "Religion": religion,
                    "Contact Number": None if contact_number == "" else contact_number,
                    "Email": None if email == "" else email,
                    "Father": father,
                    "Mother": mother,
                    "Spouse": None if spouse == "" else spouse
                    },
                "Dependents": dependent_df.to_dict(orient="records"),
                "Income": income_df.to_dict(orient="records"),
                "Health Concerns": concern_df.to_dict(orient="records"),
                "Education": education_df.to_dict(orient="records"),
                }
                confirmation(summary)

@st.experimental_dialog("Confirmation", width="large")
def confirmation(summary):
    table_name_list = ["Personal Information", "Dependents", "Income", "Health Concerns", "Education"]
    for table_name in table_name_list:
        table_name_df = pd.DataFrame([summary[table_name]] if table_name == "Personal Information" else [summary for summary in summary[table_name]]) 
        st.write(f"### {table_name}")
        if table_name_df.empty:
            st.write("No record will be added for this category.") 
        else: 
            st.dataframe(table_name_df, hide_index=True, use_container_width=True)

    st.divider()
    confirm_btn = st.button("Confirm")

    if confirm_btn:
        s = summary["Personal Information"]
        senior_data = {
            "name": s["Name"],
            "address": s["Address"],
            "birthdate": s["Birthdate"],
            "birthplace": s["Birthplace"],
            "status": s["Status"],
            "sex": s["Sex"],
            "blood_type": s["Blood Type"],
            "religion": s["Religion"],
            "contact_number": s["Contact Number"],
            "email": s["Email"],
            "father": s["Father"],
            "mother": s["Mother"],
            "spouse": s["Spouse"],
        }
        reference_code = sm.insert_senior(senior_data) 

        # Insert dependents
        for dep in summary["Dependents"]:
            dep["reference_code"] = reference_code
            sm.insert_dependent(dep)

        # Insert income
        for inc in summary["Income"]:
            inc["reference_code"] = reference_code
            sm.insert_income(inc)

        # Insert health concerns
        for health in summary["Health Concerns"]:
            health["reference_code"] = reference_code
            sm.insert_health_concern(health)

        # Insert education
        for edu in summary["Education"]:
            edu["reference_code"] = reference_code
            sm.insert_education(edu)

        st.success("Record added successfully!", icon="✅")
        st.page_link("main.py", label="Back to Homepage", icon="🏠")

senior_form()
