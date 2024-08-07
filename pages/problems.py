import streamlit as st
import pandas as pd
import sql_manager as sm
import plotly.express as px

st.set_page_config(
    page_title="SQL Problems",
    page_icon="🧪",
    layout="wide",
)

conn = sm.make_connection()
st.logo(image="./images/NCSC.png")
st.page_link("main.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)

st.markdown("## SQL Problems")
st.markdown("### :green-background[Simple Problems]")
with st.expander(
    "Display all records of SCs **not** born in Manila City and Taguig City.", icon="📍"
):
    query = """
            SELECT *
            FROM senior
            WHERE 
                BirthPlace NOT LIKE '%Manila%' 
                AND BirthPlace NOT LIKE '%Taguig%';
            """
    df = pd.read_sql_query(query, conn)
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.code(query, "sql")

with st.expander(
    "List dependents **under 18 years of age**.", icon=":material/18_up_rating:"
):
    query = """
            SELECT 
                DepID, 
                ReferenceCode, 
                DepName, 
                DepBirthdate,
                CAST((julianday('now') - julianday(DepBirthdate)) / 365.25 AS INTEGER) AS Age
            FROM dependent
            WHERE Age < 18;
            """
    original = """
                SELECT 
                    DepID,
                    ReferenceCode,
                    DepName,
                    DepBirthdate,
                    FLOOR(DATEDIFF(CURDATE(), DepBirthdate) / 365.25) AS Age
                FROM dependent
                WHERE Age < 18;
                """
    st.dataframe(
        pd.read_sql_query(query, conn), use_container_width=True, hide_index=True
    )
    st.write("SQLite:")
    st.code(query, "sql")
    st.write("Original query:")
    st.code(original, "sql")

with st.expander("Compute SC's age (considering leap years).", icon="📅"):
    query = """
            SELECT 
                ReferenceCode, 
                Name, 
                Birthdate, 
            CAST((julianday('now') - julianday(Birthdate)) / 365.25 AS INTEGER) AS Age 
            FROM senior;
            """
    original = """
                SELECT 
                    ReferenceCode, 
                    Name, 
                    Birthdate, 
                    FLOOR(DATEDIFF(CURDATE(), Birthdate) / 365.25) AS Age 
                FROM senior;
                """
    st.dataframe(
        pd.read_sql_query(query, conn), use_container_width=True, hide_index=True
    )
    st.write("SQLite:")
    st.code(query, "sql")
    st.write("Original query:")
    st.code(original, "sql")


st.markdown("### :orange-background[Moderate Problems]")
with st.expander(
    "Count the SCs suffering from *each illness* (ConcernDetails).", icon="😷"
):
    query = """
            SELECT 
                ConcernType, 
                ConcernDetails, 
                COUNT(*) AS NumberOfSeniors 
            FROM healthconcern 
            GROUP BY ConcernType, ConcernDetails 
            ORDER BY NumberOfSeniors DESC;
            """
    df = pd.read_sql_query(query, conn)
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.code(query, "sql")

with st.expander(
    "Display the *total number* of SCs with **each civil status**.",
    icon=":material/diversity_2:",
):
    query = """
            SELECT 
                CivilStatus, 
                COUNT(*) AS NumberOfSeniors
            FROM senior
            GROUP BY CivilStatus
            ORDER BY NumberOfSeniors DESC;
            """
    df = pd.read_sql_query(query, conn)
    c1, c2 = st.columns(2, vertical_alignment="center")
    c1.dataframe(df, use_container_width=True, hide_index=True)
    fig = px.pie(
        df,
        values="NumberOfSeniors",
        names="CivilStatus",
        title="Number of Seniors by Civil Status",
    )
    c2.plotly_chart(fig)
    st.code(query, "sql")

with st.expander(
    "Calculate the **total income for each source type** earned by SCs. Display also the minimum and maximum monthly income of the SCs.",
    icon="💰",
):
    query = """
            SELECT 
                SourceOfIncome, 
                SUM(MonthlyIncome) AS TotalIncome, 
                MAX(MonthlyIncome) AS MaxMonthlyIncome, 
                MIN(MonthlyIncome) AS MinMonthlyIncome
            FROM income
            GROUP BY SourceOfIncome;
            """
    df = pd.read_sql_query(query, conn)
    c1, c2 = st.columns(2, vertical_alignment="center")
    c1.dataframe(df, use_container_width=True, hide_index=True)
    df_melted = df.melt(
        id_vars=["SourceOfIncome"],
        value_vars=["TotalIncome", "MaxMonthlyIncome", "MinMonthlyIncome"],
        var_name="IncomeType",
        value_name="Income",
    )
    fig = px.bar(
        df_melted,
        x="SourceOfIncome",
        y="Income",
        color="IncomeType",
        barmode="group",
        title="Income Distribution by Source of Income",
    )
    c2.plotly_chart(fig)
    # c2.bar_chart(df, x="SourceOfIncome", y="TotalIncome", horizontal=True)
    st.code(query, "sql")

with st.expander("Count *bloodtype* by **sex and total**.", icon="🩸"):
    query = """
            SELECT 
                BloodType, 
                COUNT(CASE WHEN SexAtBirth = 'Male' THEN 1 END) AS MaleCount, 
                COUNT(CASE WHEN SexAtBirth = 'Female' THEN 1 END) AS FemaleCount, 
                COUNT(*) AS TotalCount 
            FROM senior 
            GROUP BY BloodType;
            """
    df = pd.read_sql_query(query, conn)
    c1, c2 = st.columns(2, vertical_alignment="center")
    c1.dataframe(df, use_container_width=True, hide_index=True)
    df_melted = df.melt(
        id_vars=["BloodType"],
        value_vars=["MaleCount", "FemaleCount"],
        var_name="Gender",
        value_name="Count",
    )
    fig = px.bar(
        df_melted,
        x="BloodType",
        y="Count",
        color="Gender",
        title="Blood Type Distribution by Gender",
        orientation="h",
    )
    c2.plotly_chart(fig)
    st.code(query, "sql")

st.markdown("### :red-background[Difficult Problems]")
with st.expander(
    "List seniors who have a *total monthly income of more than Php 100,000* from **all their income sources**.",
    icon="💸",
):
    query = """
            SELECT 
                Name, 
                SUM(MonthlyIncome) AS TotalIncome 
            FROM 
                senior AS S, 
                income as I 
            WHERE S.ReferenceCode = I.ReferenceCode 
            GROUP BY Name 
            HAVING SUM(MonthlyIncome) > 100000 
            ORDER BY TotalIncome DESC;
            """
    df = pd.read_sql_query(query, conn)
    c1, c2 = st.columns(2, vertical_alignment="center")
    c1.dataframe(df, use_container_width=True, hide_index=True)
    c2.bar_chart(df, x="Name", y="TotalIncome", horizontal=True)
    st.code(query, "sql")

with st.expander(
    "List the names of SCs and the *total number of dependents who are not working*, where the senior has **more than two such dependents**.",
    icon="⚒️",
):
    query = """
            SELECT 
                S.Name, 
                COUNT(D.DepID) AS NonWorkingDependents 
            FROM senior AS S, dependent AS D 
            WHERE 
                S.ReferenceCode = D.ReferenceCode
                AND D.DepIsWorking = 0 
            GROUP BY S.Name 
            HAVING COUNT(D.DepID) >= 3;"""
    df = pd.read_sql_query(query, conn)
    c1, c2 = st.columns(2, vertical_alignment="center")
    c1.dataframe(df, use_container_width=True, hide_index=True)
    c2.bar_chart(df, x="Name", y="NonWorkingDependents", horizontal=True)
    st.code(query, "sql")

with st.expander(
    "List all SCs who have *no spouse*, but **has someone dependent** to them.",
    icon="👨‍👩‍👦",
):
    query = """
            SELECT 
                S.ReferenceCode, 
                S.Name 
            FROM senior AS S 
            WHERE 
                S.ReferenceCode IN (
                    SELECT DISTINCT D.ReferenceCode 
                    FROM dependent AS D 
                    WHERE D.ReferenceCode = S.ReferenceCode
                ) 
                AND (
                    S.SpouseName IS NULL 
                    OR S.SpouseName = ''
                );
            """
    st.dataframe(
        pd.read_sql_query(query, conn), use_container_width=True, hide_index=True
    )
    st.code(query, "sql")
