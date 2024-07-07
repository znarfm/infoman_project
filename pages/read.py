import streamlit as st
import datetime
import pandas as pd
import sql_manager as sm

st.set_page_config(
    page_title="Record Information",
    page_icon="🧓",
    layout="wide",
)

conn = sm.make_connection()
st.logo(image="./images/NCSC.png")
st.page_link("main.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)

table = st.session_state.selected_table
selected = st.session_state.referencecode
senior_query = f'SELECT * FROM {table} WHERE referencecode = "{selected}";'
senior = pd.read_sql_query(senior_query, conn)
senior['CivilStatus'] = senior['CivilStatus'].apply(lambda x: 'Married' if x == 'M' else 'Single' if x == 'S' else 'Widowed' if x == 'W' else 'Separated')
senior['SexAtBirth'] = senior['SexAtBirth'].apply(lambda x: 'Male' if x == 'M' else 'Female')
dep_query = f'SELECT DepID, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate FROM dependent WHERE referencecode = "{selected}";'
dep = pd.read_sql_query(dep_query, conn)
dep['DepIsChild'] = dep['DepIsChild'].apply(lambda x: 'YES' if x == 1 else 'NO')
dep['DepIsWorking'] = dep['DepIsWorking'].apply(lambda x: 'YES' if x == 1 else 'NO')
dep = dep.rename(columns={
    'DepID': "Dependent's ID",
    'DepName': 'Dependent Name',
    'DepIsChild': 'Child of the Senior?',
    'DepIsWorking': 'Is Dependent Working?',
    'DepOccupation': 'Occupation',
    'DepIncome': 'Income',
    'DepBirthdate': 'Birthdate'
})
income_query = f'SELECT SourceOfIncome, Occupation, MonthlyIncome FROM income WHERE referencecode = "{selected}";'
income = pd.read_sql_query(income_query, conn)
income =  income.rename(columns={
    'SourceOfIncome': 'Source of Income',
    'MonthlyIncome': 'Monthly Income' 
})
concern_query = f'SELECT ConcernType, ConcernDetails FROM healthconcern WHERE referencecode = "{selected}";'
concern =  pd.read_sql_query(concern_query, conn)
concern =  concern.rename(columns={
    'ConcernType': 'Concern Type',
    'ConcernDetails': 'Concern Detail' 
})
school_query = f'SELECT e.SchoolID, s.SchoolName, e.EducationStage, e.YearStarted, e.GraduationYear FROM education as e, school as s WHERE e.SchoolID = s.SchoolID AND e.referencecode = "{selected}";'
school = pd.read_sql_query(school_query, conn)
school = school.rename(columns={
    'SchoolID': 'School ID',
    'SchoolName': 'School Name',
    'EducationStage': 'Education Stage',
    'YearStarted': 'Year Started',
    'GraduationYear': 'Graduation Year'
})
if not senior.empty:
    name = senior.iloc[0]['Name']
    birthdate = pd.to_datetime(senior.iloc[0]['BirthDate'])
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    st.header(f"{name}'s Details", divider='grey', anchor=False)
    st.write("#### Personal Information")
    for index, row in senior.iterrows():
        col1, col2 = st.columns(2)
                
        with col1:
            st.write(f"**Reference Code:** {row['ReferenceCode']}")
            st.write(f"**Address:** {row['Address']}")
            st.write(f"**Birthdate:** {row['BirthDate']}")
            st.write(f"**Birthplace:** {row['BirthPlace']}")
            st.write(f"**Sex:** {row['SexAtBirth']}")
            st.write(f"**Name of Spouse:** {row['SpouseName'] if pd.notna(row['SpouseName']) and row['SpouseName'] != '' else 'N/A'}")
            st.write(f"**Father's Name:** {row['FatherName']}")
                            
                            
                        
        with col2:
            st.write(f"**Email:** {row['ActiveEmailAddress'] if pd.notna(row['ActiveEmailAddress']) and row['ActiveEmailAddress'] != '' else 'N/A'}")
            st.write(f"**Phone Number:** {row['PrimaryContactNum'] if pd.notna(row['PrimaryContactNum']) and row['PrimaryContactNum'] != '' else 'N/A'}")
            st.write(f"**Age:** {age}")
            st.write(f"**Civil Status:** {row['CivilStatus']}")
            st.write(f"**Blood Type:** {row['BloodType']}")
            st.write(f"**Religion:** {row['Religion']}")
            st.write(f"**Mother's Name:** {row['MotherName']}")
                            
            
    st.write("")
    if not dep.empty:
        st.write("#### Dependents")
        st.dataframe(dep, use_container_width=True, hide_index=True)
                    
    st.write("")
    if not income.empty:
        st.write("#### Economic Profile")
        st.dataframe(income, use_container_width=True, hide_index=True)
    
    st.write("")
    if not concern.empty:
        st.write("#### Health Concern")
        st.dataframe(concern, use_container_width=True, hide_index=True)
    
    st.write("")
    if not school.empty:
        st.write("#### Educational Background")
        st.dataframe(school, use_container_width=True, hide_index=True)
        
            

# st.write(st.session_state.table_pk)
# st.write(st.session_state.referencecode)