import streamlit as st
import datetime
import pandas as pd
import sql_manager as sm

st.set_page_config(
    page_title="NCSC Form",
    page_icon="📝",
    layout="wide",
)

conn = sm.make_connection()

st.logo(image="./images/NCSC.png")
st.page_link("pages/add.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)

def confirmation(summary):
    st.write(summary)

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
        st.write(senior_data)
        reference_code = sm.insert_senior(senior_data) 

        # Insert dependents
        for dep in summary["Dependents"]:
            dep["reference_code"] = reference_code
            sm.insert_dependent(dep)

        # Insert income
        for inc in summary["Income"]:
            inc["reference_code"] = reference_code
            st.write(inc)
            sm.insert_income(inc)

        # Insert health concerns
        for health in summary["Health Concerns"]:
            health["reference_code"] = reference_code
            sm.insert_health_concern(health)

        # Insert education
        for edu in summary["Education"]:
            edu["reference_code"] = reference_code
            sm.insert_education(edu)

def main():
    confirmation(st.session_state.summary)

main()