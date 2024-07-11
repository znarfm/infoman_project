import streamlit as st
import datetime
import pandas as pd
import sql_manager as sm

st.set_page_config(
    page_title="Create record",
    page_icon="➕",
    layout="wide",
)

conn = sm.make_connection()
st.logo(image="./images/NCSC.png")
st.page_link("main.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)

seniors_df = pd.read_sql_query("SELECT ReferenceCode, Name FROM senior;", conn)
seniors_df["Display"] = (
    seniors_df["Name"] + " (" + seniors_df["ReferenceCode"].astype(str) + ")"
).tolist()

selected = st.selectbox("Choose a senior", options=seniors_df["Display"], index=0)
selected_code = seniors_df[seniors_df["Display"] == selected]["ReferenceCode"].values[0]
selected_code = int(selected_code)

def add_record():
    with st.form("senior_form"):
        with st.expander("Children or Dependent Information", expanded=True, icon="👪"):
            dependent_df = pd.DataFrame(
                columns=[
                    "Name",
                    "Is Child",
                    "Is Working",
                    "Occupation",
                    "Income",
                    "Birthdate",
                ]
            )
            dependent_df = st.data_editor(
                data=dependent_df,
                column_config={
                    "Name": st.column_config.TextColumn("Name", required=True),
                    "Is Child": st.column_config.CheckboxColumn(
                        "Is a children of the SC?", required=True, default=False
                    ),
                    "Is Working": st.column_config.CheckboxColumn(
                        "Is currently working?", required=True, default=False
                    ),
                    "Occupation": st.column_config.TextColumn("Occupation"),
                    "Income": st.column_config.NumberColumn("Income", min_value=0),
                    "Birthdate": st.column_config.DateColumn(
                        "Birthdate",
                        format="YYYY-MM-DD",
                        min_value=datetime.date(1900, 1, 1),
                        max_value=datetime.date.today(),
                        required=True,
                    ),
                },
                num_rows="dynamic",
                use_container_width=True,
            )

        with st.expander("Income Information", expanded=True, icon="🪙"):
            income_df = pd.DataFrame(columns=["Source", "Occupation", "Amount"])
            income_df = st.data_editor(
                data=income_df,
                column_config={
                    "Source": st.column_config.SelectboxColumn(
                        "Source",
                        options=[
                            "Salary",
                            "Pension",
                            "Business",
                            "Insurance",
                            "Savings",
                            "Stocks",
                        ],
                        required=True,
                    ),
                    "Occupation": st.column_config.TextColumn("Occupation"),
                    "Amount": st.column_config.NumberColumn(
                        "Amount", min_value=0, required=True
                    ),
                },
                num_rows="dynamic",
                use_container_width=True,
            )

        with st.expander("Health Concerns", expanded=True, icon="🩺"):
            concern_df = pd.DataFrame(columns=["Type", "Details"])
            concern_df = st.data_editor(
                data=concern_df,
                column_config={
                    "Type": st.column_config.SelectboxColumn(
                        "Type",
                        options=["Medical", "Dental", "Vision", "Hearing", "Social"],
                        required=True,
                    ),
                    "Details": st.column_config.TextColumn("Details", required=True),
                },
                num_rows="dynamic",
                use_container_width=True,
            )

        with st.expander("Educational Information", expanded=True, icon="🎓"):
            schools_df = pd.read_sql_query(
                "SELECT SchoolID, SchoolName FROM school ORDER BY SchoolName", conn
            )
            schools = schools_df["SchoolName"].to_list()
            education_df = pd.DataFrame(
                columns=[
                    "Education Level",
                    "School Name",
                    "Year Started",
                    "Year Completed",
                ]
            )
            education_df = st.data_editor(
                data=education_df,
                column_config={
                    "Education Level": st.column_config.SelectboxColumn(
                        "Level",
                        options=["Primary", "Secondary", "Tertiary"],
                        required=True,
                    ),
                    "School Name": st.column_config.SelectboxColumn(
                        "School Name", options=schools, required=True
                    ),
                    "Year Started": st.column_config.NumberColumn(
                        "Year Started",
                        format="%f",
                        required=True,
                        min_value=1900,
                        max_value=datetime.date.today().year,
                    ),
                    "Year Completed": st.column_config.NumberColumn(
                        "Year Completed",
                        format="%f",
                        required=True,
                        min_value=1900,
                        max_value=datetime.date.today().year,
                    ),
                },
                num_rows="dynamic",
                use_container_width=True,
            )

        submitted = st.form_submit_button("Submit")
        if submitted:
            education_df["SchoolID"] = education_df["School Name"].apply(
                lambda x: schools_df[schools_df["SchoolName"] == x][
                    "SchoolID"
                ].values[0]
            )
            summary = {
                "Dependents": dependent_df.to_dict(orient="records"),
                "Income": income_df.to_dict(orient="records"),
                "Health Concerns": concern_df.to_dict(orient="records"),
                "Education": education_df.to_dict(orient="records"),
            }
            confirmation(summary)


@st.experimental_dialog("Confirmation", width="large")
def confirmation(summary):
    table_name_list = [
        "Dependents",
        "Income",
        "Health Concerns",
        "Education",
    ]
    for table_name in table_name_list:
        table_name_df = pd.DataFrame(summary[table_name])
        st.write(f"### {table_name}")
        if table_name_df.empty:
            st.write("No record will be added for this category.")
        else:
            st.dataframe(table_name_df, hide_index=True, use_container_width=True)

    st.divider()
    confirm_btn = st.button("Confirm")

    if confirm_btn:
        # Insert dependents
        for dep in summary["Dependents"]:
            dep["reference_code"] = selected_code
            sm.insert_dependent(dep)

        # Insert income
        for inc in summary["Income"]:
            inc["reference_code"] = selected_code
            sm.insert_income(inc)

        # Insert health concerns
        for health in summary["Health Concerns"]:
            health["reference_code"] = selected_code
            sm.insert_health_concern(health)

        # Insert education
        for edu in summary["Education"]:
            edu["reference_code"] = selected_code
            sm.insert_education(edu)

        st.success("Record added successfully!", icon="✅")
        st.page_link("main.py", label="Back to Homepage", icon="🏠")


add_record()