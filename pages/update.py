import streamlit as st
import datetime
import sql_manager as sm
import pandas as pd

st.set_page_config(
    page_title="Update Record",
    page_icon="✍️",
    layout="wide",
)

conn = sm.make_connection()
st.logo(image="./images/NCSC.png")
st.page_link("main.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)

table_selected = st.session_state.selected_table

match table_selected:
    case "Senior":
        st.markdown(f"### {table_selected} Table")
        df = pd.read_sql_query(
            f"SELECT * FROM {table_selected} WHERE referencecode = {st.session_state.referencecode};",
            conn,
        )
        df_to_edit = df.drop(columns=["ReferenceCode"])
        edited_df = st.data_editor(
            df_to_edit, hide_index=True, use_container_width=True
        )
        upd_btn = st.button("UPDATE")
        if upd_btn:
            table = st.session_state.selected_table.lower()

            try:
                sm.update_senior(
                    table, edited_df, st.session_state.referencecode, "referencecode"
                )
                st.success("Record updated successfully!")
            except Exception as e:
                st.error(f"Error updating record: {e}")

    case "Education":
        st.markdown(f"### {table_selected} Table")
        schools_df = pd.read_sql_query(
            "SELECT SchoolID, SchoolName FROM school ORDER BY SchoolName", conn
        )
        school_ids = schools_df["SchoolID"].tolist()

        df = pd.read_sql_query(
            f"SELECT * FROM {table_selected} WHERE referencecode = {st.session_state.referencecode};",
            conn,
        )
        df_to_edit = df.drop(columns=["EducID", "ReferenceCode"])
        edited_df = st.data_editor(
            data=df_to_edit,
            column_config={
                "EducationStage": st.column_config.SelectboxColumn(
                    options=["Primary", "Secondary", "Tertiary"], required=True
                ),
                "SchoolID": st.column_config.SelectboxColumn(
                    options=school_ids, required=True
                ),
                "YearStarted": st.column_config.NumberColumn(
                    format="%f",
                    required=True,
                    min_value=1900,
                    max_value=datetime.date.today().year,
                ),
                "YearCompleted": st.column_config.NumberColumn(
                    format="%f",
                    required=True,
                    min_value=1900,
                    max_value=datetime.date.today().year,
                ),
            },
            use_container_width=True,
            hide_index=True,
        )
        upd_btn = st.button("Update")
        if upd_btn:
            table = st.session_state.selected_table.lower()

            for index, row in edited_df.iterrows():
                try:
                    specific_value = df.iloc[index]["EducID"]
                    sm.update_record(table, row, specific_value, "EducID")
                    st.success(f"Record {index + 1} updated successfully!")
                except Exception as e:
                    st.error(f"Error updating record {index}: {e}")

    case "Health Concern":
        st.markdown(f"### {table_selected} Table")
        df = pd.read_sql_query(
            f"SELECT * FROM healthconcern WHERE referencecode = {st.session_state.referencecode};",
            conn,
        )
        df_to_edit = df.drop(columns=["ConcernID", "ReferenceCode"])
        edited_df = st.data_editor(
            data=df_to_edit,
            column_config={
                "ConcernType": st.column_config.SelectboxColumn(
                    options=["Medical", "Dental", "Vision", "Hearing", "Social"],
                    required=True,
                ),
                "ConcernDetails": st.column_config.TextColumn(required=True),
            },
            use_container_width=True,
            hide_index=True,
        )
        upd_btn = st.button("UPDATE")
        if upd_btn:
            table = "healthconcern"

            for index, row in edited_df.iterrows():
                try:
                    specific_value = df.iloc[index]["ConcernID"]
                    sm.update_record(table, row, specific_value, "ConcernID")
                    st.success(f"Record {index + 1} updated successfully!")
                except Exception as e:
                    st.error(f"Error updating record {index}: {e}")

    case "Income":
        st.markdown(f"### {table_selected} Table")
        df = pd.read_sql_query(
            f"SELECT * FROM {table_selected} WHERE referencecode = {st.session_state.referencecode};",
            conn,
        )
        df_to_edit = df.drop(columns=["IncomeID", "ReferenceCode"])
        edited_df = st.data_editor(
            data=df_to_edit,
            column_config={
                "SourceOfIncome": st.column_config.SelectboxColumn(
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
                "MonthlyIncome": st.column_config.NumberColumn(
                    min_value=0, required=True
                ),
            },
            use_container_width=True,
            hide_index=True,
        )
        upd_btn = st.button("UPDATE")
        if upd_btn:
            table = st.session_state.selected_table.lower()

            for index, row in edited_df.iterrows():
                try:
                    specific_value = df.iloc[index]["IncomeID"]
                    sm.update_record(table, row, specific_value, "IncomeID")
                    st.success(f"Record {index + 1} updated successfully!")
                except Exception as e:
                    st.error(f"Error updating record {index}: {e}")

    case "Dependent":
        st.markdown(f"### {table_selected} Table")
        df = pd.read_sql_query(
            f"SELECT * FROM {table_selected} WHERE referencecode = {st.session_state.referencecode};",
            conn,
        )
        df["DepBirthdate"] = pd.to_datetime(df["DepBirthdate"], errors="coerce")
        df_to_edit = df.drop(columns=["DepID", "ReferenceCode"])
        edited_df = st.data_editor(
            data=df_to_edit,
            column_config={
                "DepName": st.column_config.TextColumn(required=True),
                "DepIsChild": st.column_config.CheckboxColumn(required=True),
                "DepIsWorking": st.column_config.CheckboxColumn(required=True),
                "DepOccupation": st.column_config.TextColumn("Occupation"),
                "DepIncome": st.column_config.NumberColumn("Income", min_value=0),
                "DepBirthdate": st.column_config.DateColumn(
                    format="YYYY-MM-DD",
                    min_value=datetime.date(1900, 1, 1),
                    max_value=datetime.date.today(),
                    required=True,
                ),
            },
            use_container_width=True,
            hide_index=True,
        )
        upd_btn = st.button("UPDATE")
        if upd_btn:
            table = st.session_state.selected_table.lower()

            for index, row in edited_df.iterrows():
                try:
                    specific_value = df.iloc[index]["DepID"]
                    row["DepBirthdate"] = row["DepBirthdate"].strftime("%Y-%m-%d")
                    sm.update_record(table, row, specific_value, "DepID")
                    st.success(f"Record {index + 1} updated successfully!")
                except Exception as e:
                    st.error(f"Error updating record {index}: {e}")

    case "School":
        st.markdown(f"### {table_selected} Table")
        df = pd.read_sql_query(
            f"SELECT * FROM {table_selected} WHERE SchoolID = {st.session_state.referencecode};",
            conn,
        )
        df_to_edit = df.drop(columns=["SchoolID"])
        edited_df = st.data_editor(
            df_to_edit,
            hide_index=True,
            use_container_width=True,
            column_config={
                "SchoolName": st.column_config.TextColumn(required=True),
                "SchoolAddress": st.column_config.TextColumn(required=True),
            },
        )
        upd_btn = st.button("UPDATE")
        if upd_btn:
            table = st.session_state.selected_table.lower()

            try:
                sm.update_senior(
                    table, edited_df, st.session_state.referencecode, "SchoolID"
                )
                st.success("Record updated successfully!")
            except Exception as e:
                st.error(f"Error updating record: {e}")
