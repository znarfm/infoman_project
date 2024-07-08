import streamlit as st
import sql_manager as sm
import pandas as pd
from streamlit_extras.bottom_container import bottom
import datetime

st.set_page_config(
    page_title="National Commission of Senior Citizens",
    page_icon="./images/NCSC.png",
    layout="wide",
    # initial_sidebar_state="collapsed",
)

conn = sm.make_connection()
st.logo(image="./images/NCSC.png")
st.sidebar.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)


table_name_mapping = {
    "Senior": "senior",
    "Education": "education",
    "Health Concern": "healthconcern",
    "Income": "income",
    "Dependent": "dependent",
    "School": "school",
}

st.sidebar.warning("Application is still under development.", icon="⚠️")

def view_tables():
    # Select a specific table
    selected_table = st.sidebar.selectbox(
        "Select a table",
        table_name_mapping.keys(),
    )
    st.session_state.selected_table = selected_table

    name_code_df = pd.read_sql_query("SELECT ReferenceCode, Name FROM senior", conn)
    name_code_df["Display"] = name_code_df['Name'] + " (" + name_code_df['ReferenceCode'].astype(str) + ")"
    senior_options = ["All"] + name_code_df["Display"].tolist()     # Prepend "all" to the list of options

    selected_senior = st.sidebar.selectbox(
        "Filter to show records for a specific senior",
        senior_options,
        index=0,
        disabled=st.session_state.selected_table == "School",
    )

    if selected_senior != "All":
        selected_code = name_code_df[name_code_df["Display"] == selected_senior]["ReferenceCode"].values[0]
        st.session_state.selected_code = selected_code
    else:
        st.session_state.selected_code = None

    # Display the table
    if selected_table:
        v_selected_table = table_name_mapping[selected_table]
        st.write(f"### {selected_table}")


        if st.session_state.selected_code and selected_table != "School":
            df = pd.read_sql_query(f"SELECT * FROM {v_selected_table} WHERE ReferenceCode = '{st.session_state.selected_code}'", conn)
        else:
            df = pd.read_sql_query(f"SELECT * FROM {v_selected_table}", conn)

        # Remove , from keys
        if selected_table in ["Senior", "School"]:
            df.iloc[:, 0] = df.iloc[:, 0].astype(str)
        else:
            df.iloc[:, :2] = df.iloc[:, :2].astype(str)

        if selected_table == "Dependent":
            colconfig = {
                "DepIsChild": st.column_config.CheckboxColumn("Dependent is children of SC"),
                "DepIsWorking": st.column_config.CheckboxColumn("Dependent is working"),
            }
        else:
            colconfig = {}

        event = st.dataframe(df, 
                    use_container_width=True, 
                    hide_index=True,
                    selection_mode="single-row",
                    on_select="rerun",
                    column_config=colconfig
                    )
        
        st.markdown("### Selected Record")
        sel = event.selection.rows
        selected_row_df = df.iloc[sel]
        if not selected_row_df.empty:
            # For debugging
            st.dataframe(selected_row_df, 
                    use_container_width=True, 
                    hide_index=True,
                    )
            st.session_state.referencecode = selected_row_df["ReferenceCode"].values[0] if selected_table != "School" else selected_row_df["SchoolID"].values[0]
            st.session_state.table_pk = selected_row_df.iloc[0].values[0]

    st.sidebar.divider()
    st.sidebar.markdown("### Operations")
    if selected_table == "Senior":
        st.sidebar.page_link("pages/add.py", label="Create new record", icon="📝")
        st.sidebar.page_link("pages/read.py", label="Read selected record", icon="🔎", disabled=selected_row_df.empty)
    if selected_table == "School":
        st.sidebar.page_link("pages/add_school.py", label="Add new school", icon="🏫")
    st.sidebar.page_link("pages/update.py", label="Update selected record", icon="✍️", disabled=selected_row_df.empty)
    st.sidebar.page_link("pages/delete.py", label="Delete selected record", icon="🗑️", disabled=selected_row_df.empty)
    st.sidebar.divider()
    st.sidebar.page_link("pages/about.py", label="About", icon="❓")
    
    with bottom():
        st.info("This website is intended solely for academic purposes.", icon="📙")

view_tables()

