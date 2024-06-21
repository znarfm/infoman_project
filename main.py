import streamlit as st
import datetime

st.set_page_config(
    page_title="National Commission of Senior Citizens",
    page_icon="🏠",
    layout="wide",
    # initial_sidebar_state="collapsed",
)

conn = st.connection('mysql', type='sql')
st.image('https://dswdprogram.com/wp-content/uploads/2023/05/ncsc-logo-768x777.jpg', width=150)
st.title("National Commission of Senior Citizens")
st.divider()
mode = st.sidebar.selectbox("Select operation", ["View Tables", "Create", "Read", "Update", "Delete"])

def create():
    if 'dependents' not in st.session_state:
        st.session_state.dependents = []

    def add_dependent():
        st.session_state.dependents.append({
            'name': st.session_state.dep_name,
            'is_child': st.session_state.dep_is_child,
            'is_working': st.session_state.dep_is_working,
            'occupation': st.session_state.dep_occupation,
            'income': st.session_state.dep_income,
        })

    with st.form("senior_form"):
        st.write("# Senior Citizen Form")

        info_exp = st.expander("Personal Information", expanded=True)
        with info_exp:
            name = st.text_input("Full Name")
            address = st.text_input("Address")

            col1, col2 = st.columns(2)
            with col1:
                birthdate = st.date_input("Birthdate", value=None, format="YYYY-MM-DD", min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today() - datetime.timedelta(days=60*365.25))
            with col2:
                birthplace = st.text_input("Birthplace")

            col1, col2, col3 = st.columns(3)
            with col1: 
                status = st.selectbox("Status", ["Single", "Married", "Separated", "Widowed"], index=None)
            with col2:
                sex = st.selectbox("Sex", ["Male", "Female"], index=None)
            with col3:
                blood_type = st.selectbox("Blood Type", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], index=None)
            
            religion = st.text_input("Religion")

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
            dep_is_child = st.radio("Is the dependent a children of the Senior Citizen", ["Yes", "No"])
            dep_is_working = st.radio("Is the dependent Working", ["Yes", "No"])
            dep_occupation = st.text_input("Dependent's Occupation")
            dep_income = st.number_input("Dependent's Income", min_value=0)
            dep_birthdate = st.date_input("Dependent's Birthdate", value=None, format="YYYY-MM-DD", min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())

        income_exp = st.expander("Income Information", expanded=True)
        with income_exp:
            source = st.selectbox("Source of Income", ["Salary", "Pension", "Business", "Insurance", "Savings", "Stocks"], index=None)
            occupation = st.text_input("Occupation")
            income = st.number_input("Monthly Income", min_value=0)

        health_exp = st.expander("Health Concerns", expanded=True)
        with health_exp:
            concern_type = st.selectbox("Type of Concern", ["Medical", "Dental", "Optical", "Hearing", "Social"], index=None)
            con_details = st.text_input("Details of Concern")

        educ_exp = st.expander("Educational Information", expanded=True)
        with educ_exp:
            edu_level = st.selectbox("Highest Level of Education", ["Primary", "Secondary", "Tertiary", "Graduate", "Post-Graduate", "Doctorate"], index=None)


        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Submitted!")


def view_tables():
    tables = conn.query("SHOW TABLES;", ttl=600)
    selected_table = st.selectbox("Select a table", [word.capitalize() for word in tables.values.tolist()])
    st.write("Selected table: ", selected_table)

    df = conn.query(f'SELECT * FROM {selected_table};', ttl=600)
    st.dataframe(df, use_container_width=True, hide_index=True)

def read():
    df = conn.query('SELECT name FROM senior ORDER BY name;', ttl=600)

    st.dataframe(df, hide_index=True, use_container_width=True)

# TODO: this function needs to be updated
def show_individual(id):
    df = conn.query(f'SELECT * FROM senior WHERE id = {id};', ttl=600)

def update():
    pass

def delete():
    pass


if mode == "Create":
    create()
elif mode == "Read":
    read()
elif mode == "Update":
    update()
elif mode == "Delete":
    delete()
elif mode == "View Tables":
    view_tables()