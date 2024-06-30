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
    if "selected_table" not in st.session_state:
        selected_table = st.sidebar.selectbox(
            "Select a table",
            table_name_mapping.keys(),
        )
        st.session_state.table = selected_table

    # Filter rows for a specific senior
    seniors_df = sm.show_table(conn, "senior")
    seniors_df["Display"] = seniors_df['Name'] + " (" + seniors_df['ReferenceCode'].astype(str) + ")"
    if "selected_senior" not in st.session_state:
        selected_senior = st.sidebar.selectbox(
            "Filter to show records for a specific senior",
            seniors_df["Display"],
            index=None
        )
        if selected_senior:
            selected_senior = seniors_df[seniors_df["Display"] == selected_senior]["ReferenceCode"].values[0]
            st.session_state.referencecode = selected_senior

    st.sidebar.divider()
    st.sidebar.markdown("### Operations")
    if selected_table == "Senior":
        st.sidebar.page_link("pages/add.py", label="Create new record", icon="📝")
        st.sidebar.page_link("pages/read.py", label="Read selected record", icon="🔎")
    st.sidebar.page_link("pages/update.py", label="Update selected record", icon="✍️")
    st.sidebar.page_link("pages/delete.py", label="Delete selected record", icon="🗑️")
    # create_btn = st.sidebar.button("Create new record")
    # read_btn = st.sidebar.button("Read selected record") if selected_table == "Senior" else None
    # update_btn = st.sidebar.button("Update selected record")
    # delete_btn = st.sidebar.button("Delete selected record")

    if selected_table:
        v_selected_table = table_name_mapping[selected_table]
        st.write(f"### {selected_table}")
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
                st.session_state["referencecode"] = selected_row_df["ReferenceCode"].values[0]

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
