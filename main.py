import streamlit as st
from streamlit_free_text_select import st_free_text_select
import datetime
import sql_manager as sm

st.set_page_config(
    page_title="National Commission of Senior Citizens",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

conn = sm.make_connection("mysql", "sql")
st.image("./images/NCSC.png", width=100)
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)
mode = st.sidebar.radio(
    "Select operation", ["View Tables", "Create", "Read", "Update", "Delete"]
)

table_name_mapping = {
    "Dependent": "dependent",
    "Education": "education",
    "Health Concern": "healthconcern",
    "Income": "income",
    "School": "school",
    "Senior": "senior"
}

def create():
    st.markdown("## Create/add a new record")
    with st.form("senior_form"):
        st.write("### Senior Citizen Form")

        info_exp = st.expander("Personal Information", expanded=True)
        with info_exp:
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

        dep_exp = st.expander("Children or Dependent Information", expanded=True)
        with dep_exp:
            dep_name = st.text_input("Dependent Name")
            dep_is_child = st.radio(
                "Is the dependent a children of the Senior Citizen", ["Yes", "No"]
            )
            dep_is_working = st.radio("Is the dependent Working", ["Yes", "No"])
            dep_occupation = st.text_input("Dependent's Occupation")
            dep_income = st.number_input("Dependent's Income", min_value=0)
            dep_birthdate = st.date_input(
                "Dependent's Birthdate",
                value=None,
                format="YYYY-MM-DD",
                min_value=datetime.date(1900, 1, 1),
                max_value=datetime.date.today(),
            )

        income_exp = st.expander("Income Information", expanded=True)
        with income_exp:
            source = st.multiselect(
                "Source of Income",
                ["Salary", "Pension", "Business", "Insurance", "Savings", "Stocks"],
            )
            occupation = st.text_input("Occupation")
            income = st.number_input("Monthly Income", min_value=0)

        health_exp = st.expander("Health Concerns", expanded=True)
        with health_exp:
            concern_type = st.selectbox(
                "Type of Concern",
                ["Medical", "Dental", "Optical", "Hearing", "Social"],
                index=None,
            )
            con_details = st.text_input("Details of Concern")

        educ_exp = st.expander("Educational Information", expanded=True)
        with educ_exp:
            edu_level = st.selectbox(
                "Highest Level of Education",
                [
                    "Primary",
                    "Secondary",
                    "Tertiary",
                    "Graduate",
                    "Post-Graduate",
                    "Doctorate",
                ],
                index=None,
            )
            sch_name = st.text_input("School Name").upper()
            sch_address = st.text_input("School Address")

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Submitted!")


def view_tables():
    st.write("## View Tables")
    selected_table = st.selectbox(
        "Select a table",
        table_name_mapping.keys(),
    )

    if selected_table:
        v_selected_table = table_name_mapping[selected_table]
        st.write(f"### {selected_table}")
        df = sm.show_table(conn, v_selected_table)
        st.dataframe(df, use_container_width=True, hide_index=True)

# Bryll
def read():
    search = None
    st.write("## Read/view data of specific record")
    search = st.text_input("Search for a name of a senior citizen")
    search_df = conn.query(
        f'SELECT name, referencecode FROM senior WHERE name LIKE "%{search}%" ORDER BY name;',
        ttl=600,
    )

    if not search_df.empty:
        search_df["formatted"] = search_df.apply(
            lambda x: f"{x['name']} ({x['referencecode']})", axis=1
        )
        options = search_df["formatted"].tolist()
        mapping = dict(zip(search_df["formatted"], search_df["referencecode"]))

        st.divider()

        c1, c2 = st.columns([1, 3])

        with c1:
            selected_option = st.radio("Select a Senior Citizen", options)

        with c2:
            if selected_option:
                selected_id = mapping[selected_option]
                selected_df = conn.query(
                    f'SELECT * FROM senior WHERE referencecode = "{selected_id}";',
                    ttl=600,
                )
                st.dataframe(selected_df, hide_index=True, use_container_width=True)


# Bryll
def update():
    st.write("## Update a record")
    search = st.text_input("Search for a name of a senior citizen")
    if search:
        search_df = sm.search_senior(conn, search)

        # if not search_df.empty:
        search_df["formatted"] = search_df.apply(
            lambda x: f"{x['name']} ({x['referencecode']})", axis=1
        )
        options = search_df["formatted"].tolist()
        mapping = dict(zip(search_df["formatted"], search_df["referencecode"]))

        st.divider()
        if search_df.empty:
            st.write("No records found")
        else:
            c1, c2 = st.columns([1, 3])
            with c1:
                    selected_option = st.radio("Select a Senior Citizen", options)
            with c2:
                if selected_option:
                    selected_id = mapping[selected_option]
                    sel_table = st.selectbox("Select a table", ["Senior", "Dependent"])

                    sel_info_df = conn.query(
                        f'SELECT * FROM {sel_table} WHERE referencecode = "{selected_id}";',
                        ttl=600,
                    )
                    st.markdown(f"### {sel_table.capitalize()}")
                    st.data_editor(sel_info_df, hide_index=True, use_container_width=True)

                    # sel_dep_df = conn.query(f'SELECT * FROM dependent WHERE referencecode = "{selected_id}";', ttl=600)
                    # st.markdown("### Dependent / Children Information")
                    # st.data_editor(sel_dep_df, hide_index=True, use_container_width=True, num_rows="dynamic")


# TODO
def delete():
    st.write("## Delete a record")
    seniors = conn.query("SELECT name, referencecode FROM senior ORDER BY name;", ttl=600)
    search = st_free_text_select("Search for a name of a senior citizen",
                                 options=seniors["name"].tolist())
    if search:
        st.write(search)

def experimental_delete():
    st.write("## Delete a record from tables")
    
    
match mode:
    case "Create":
        create()
    case "Read":
        read()
    case "Update":
        update()
    case "Delete":
        experimental_delete()
    case "View Tables":
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
