import streamlit as st
from streamlit_free_text_select import st_free_text_select
import datetime
import sql_manager as sm

st.set_page_config(
    page_title="National Commission of Senior Citizens",
    page_icon="🏠",
    layout="wide",
    # initial_sidebar_state="collapsed",
)

conn = sm.make_connection("mysql", "sql")
st.sidebar.image("./images/NCSC.png", width=100)
st.sidebar.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)
# mode = st.sidebar.radio(
#     "Select operation", ["View Tables", "Create", "Read", "Update", "Delete"]
# )


table_name_mapping = {
    "Senior": "senior",
    "Education": "education",
    "Health Concern": "healthconcern",
    "Income": "income",
    "Dependent": "dependent",
    "School": "school",
}

def view_tables():
    # Select a specific table
    selected_table = st.sidebar.selectbox(
        "Select a table",
        table_name_mapping.keys(),
    )
    if "selected_table" not in st.session_state:
        st.session_state.selected_table = selected_table

    # Filter rows for a specific senior
    name_code_df = sm.get_senior_name_and_code(conn)
    name_code_df["Display"] = name_code_df['Name'] + " (" + name_code_df['ReferenceCode'].astype(str) + ")"

    # Prepend "all" option to the list
    senior_options = ["All"] + name_code_df["Display"].tolist()

    selected_senior = st.sidebar.selectbox(
        "Filter to show records for a specific senior",
        senior_options,
        index=0     # index 0 is "All"
    )
    if "selected_senior" not in st.session_state:
        st.session_state.selected_senior = selected_senior

    if selected_senior != "All":
        selected_code = name_code_df[name_code_df["Display"] == selected_senior]["ReferenceCode"].values[0]
        st.session_state.selected_code = selected_code
    else:
        st.session_state.selected_code = None





    st.sidebar.divider()
    st.sidebar.markdown("### Operations")
    if selected_table == "Senior":
        st.sidebar.page_link("pages/add.py", label="Create new record", icon="📝")
        st.sidebar.page_link("pages/read.py", label="Read selected record", icon="🔎")
    st.sidebar.page_link("pages/update.py", label="Update selected record", icon="✍️")
    st.sidebar.page_link("pages/delete.py", label="Delete selected record", icon="🗑️")

    if selected_table:
        v_selected_table = table_name_mapping[selected_table]
        st.write(f"### {selected_table}")

        if st.session_state.selected_code:
            df = sm.filter_reference_code(conn, v_selected_table, st.session_state.selected_code)
        else:
            df = sm.show_table(conn, v_selected_table)

        event = st.dataframe(df, 
                    use_container_width=True, 
                    hide_index=True,
                    selection_mode="single-row",
                    on_select="rerun",
                    )
        
        st.markdown("### Selected Record")
        sel = event.selection.rows
        selected_row_df = df.iloc[sel]
        if not selected_row_df.empty:
            st.dataframe(selected_row_df, 
                    use_container_width=True, 
                    hide_index=True,
                    )
            if "referencecode" not in st.session_state:
                st.session_state.referencecode = selected_row_df["ReferenceCode"].values[0]

view_tables()

# st.markdown("""
#     <style>
#     .footer {
#         position: fixed;
#         left: 0;
#         bottom: 0;
#         width: 100%;
#         background-color: #253C64; /* Background color */
#         color: #FFFFFF; /* Text color */
#         text-align: center;
#         font-size: 12px; /* Font size */
#         padding: 30px;
#         border-radius: 10px; /* Border radius */
#     }
#     </style>
#     <div class="footer">
#         This website is an independent project and is not affiliated with NCSC. It is intended solely for academic purposes.
#     </div>
#     """, unsafe_allow_html=True)
