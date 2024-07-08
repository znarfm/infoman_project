import sqlite3
import pandas as pd

def make_connection():
    return sqlite3.connect("projectdb.db")

def create_tables(conn):
    sql_statements = [
        "PRAGMA foreign_keys = off;",
        "BEGIN TRANSACTION;",
        """
        CREATE TABLE IF NOT EXISTS dependent (
            DepID INTEGER PRIMARY KEY AUTOINCREMENT, 
            ReferenceCode INTEGER NOT NULL, 
            DepName TEXT NOT NULL, 
            DepIsChild INTEGER CHECK(DepIsChild IN (0, 1)) NOT NULL, 
            DepIsWorking INTEGER CHECK(DepIsWorking IN (0, 1)) NOT NULL, 
            DepOccupation TEXT, 
            DepIncome REAL, 
            DepBirthdate DATE NOT NULL,
            FOREIGN KEY (ReferenceCode) REFERENCES senior (ReferenceCode)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS education (
            EducID INTEGER PRIMARY KEY AUTOINCREMENT, 
            ReferenceCode INTEGER NOT NULL, 
            SchoolID TEXT NOT NULL, 
            EducationStage TEXT CHECK(EducationStage IN ('Primary', 'Secondary', 'Tertiary')) NOT NULL, 
            YearStarted TEXT NOT NULL, 
            GraduationYear TEXT NOT NULL,
            FOREIGN KEY (ReferenceCode) REFERENCES senior (ReferenceCode),
            FOREIGN KEY (SchoolID) REFERENCES school (SchoolID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS healthconcern (
            ConcernID INTEGER PRIMARY KEY AUTOINCREMENT, 
            ReferenceCode INTEGER NOT NULL, 
            ConcernType TEXT CHECK(ConcernType IN ('Medical', 'Dental', 'Vision', 'Hearing', 'Social')) NOT NULL, 
            ConcernDetails TEXT NOT NULL,
            FOREIGN KEY (ReferenceCode) REFERENCES senior (ReferenceCode)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS income (
            IncomeID INTEGER PRIMARY KEY AUTOINCREMENT, 
            ReferenceCode INTEGER NOT NULL, 
            SourceOfIncome TEXT CHECK(SourceOfIncome IN ('Salary', 'Pension', 'Business', 'Insurance', 'Savings', 'Stocks')) NOT NULL, 
            Occupation TEXT, 
            MonthlyIncome REAL NOT NULL DEFAULT 0,
            FOREIGN KEY (ReferenceCode) REFERENCES senior (ReferenceCode)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS school (
            SchoolID INTEGER PRIMARY KEY AUTOINCREMENT,
            SchoolName TEXT NOT NULL,
            SchoolAddress TEXT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS senior (
            ReferenceCode INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Address TEXT NOT NULL,
            BirthDate DATE NOT NULL,
            BirthPlace TEXT NOT NULL,
            CivilStatus TEXT NOT NULL CHECK(CivilStatus IN ('Single', 'Married', 'Widowed', 'Separated')),
            SexAtBirth TEXT NOT NULL CHECK(SexAtBirth IN ('Male', 'Female')),
            BloodType TEXT NOT NULL CHECK(BloodType IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')),
            PrimaryContactNum TEXT,
            ActiveEmailAddress TEXT,
            Religion TEXT NOT NULL CHECK(Religion IN ('Roman Catholic', 'Islam', 'Iglesia ni Cristo', 'Jehovah''s Witnesses', 'Evangelical', 'Baptist', 'Mormon', 'Buddhist', 'Hindu', 'Others')),
            SpouseName TEXT,
            FatherName TEXT NOT NULL,
            MotherName TEXT NOT NULL
        );
        """,
        "COMMIT TRANSACTION;",
        "PRAGMA foreign_keys = on;"
    ]

    for statement in sql_statements:
        conn.execute(statement)

# INSERT statements
def insert_senior(senior_data):
    with make_connection() as conn:
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO senior (name, address, birthdate, birthplace, civilstatus, sexatbirth, bloodtype, religion, primarycontactnum, activeemailaddress, fathername, mothername, spousename)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (
            senior_data["name"],
            senior_data["address"],
            senior_data["birthdate"],
            senior_data["birthplace"],
            senior_data["status"],
            senior_data["sex"],
            senior_data["blood_type"],
            senior_data["religion"],
            senior_data["contact_number"],
            senior_data["email"],
            senior_data["father"],
            senior_data["mother"],
            senior_data["spouse"]
        ))
        conn.commit()
        lastrowid = cursor.lastrowid
        return lastrowid

def insert_dependent(dependent_data):
    with make_connection() as conn:
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO dependent (referencecode, depname, depischild, depisworking, depoccupation, depincome, depbirthdate)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (
            dependent_data["reference_code"],
            dependent_data["Name"],
            dependent_data["Is Child"],
            dependent_data["Is Working"],
            dependent_data["Occupation"],
            dependent_data["Income"],
            dependent_data["Birthdate"]
        ))
        conn.commit()

def insert_income(income_data):
    with make_connection() as conn:
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO income (referencecode, sourceofincome, occupation, monthlyincome)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(insert_query, (
            income_data["reference_code"],
            income_data["Source"],
            income_data["Occupation"],
            income_data["Amount"]
        ))
        conn.commit()

def insert_health_concern(concern_data):
    with make_connection() as conn:
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO healthconcern (referencecode, concerntype, concerndetails)
        VALUES (?, ?, ?)
        """
        cursor.execute(insert_query, (
            concern_data["reference_code"],
            concern_data["Type"],
            concern_data["Details"]
        ))
        conn.commit()

def insert_education(education_data):
    with make_connection() as conn:
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO education (referencecode, schoolid, educationstage, yearstarted, graduationyear)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (
            education_data["reference_code"],
            education_data["SchoolID"],
            education_data["Education Level"],
            education_data["Year Started"],
            education_data["Year Completed"]
        ))
        conn.commit()

def insert_school(school_data):
    with make_connection() as conn:
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO school (SchoolID, SchoolName, SchoolAddress)
        VALUES (?, ?, ?)
        """
        cursor.execute(insert_query, (
            school_data["School ID"],
            school_data["School Name"],
            school_data["School Address"]
        ))
        conn.commit()
        return True

# UPDATE statements
def update_senior(table_name, df, reference_code, pk):
    with make_connection() as conn:
        cursor = conn.cursor()
        
        # Fetch column names from DataFrame
        columns = df.columns.tolist()
        reference_code = str(reference_code)
        
        # Create the SET clause for the SQL UPDATE query
        set_clause = ", ".join([f"{col} = ?" for col in columns])
        
        # Construct the SQL UPDATE query
        update_query = f"""
        UPDATE {table_name}
        SET {set_clause}
        WHERE {pk} = ?;
        """
        
        # Iterate over each row in the DataFrame and update the corresponding record
        for index, row in df.iterrows():
            values = row.tolist() + [reference_code]
            cursor.execute(update_query, values)

        conn.commit()
        
def update_record(table_name, row, df_id, pk):
    with make_connection() as conn:
        cursor = conn.cursor()

        columns = row.index.tolist()
        df_id = str(df_id)
        
        # Create the SET clause for the SQL UPDATE query
        set_clause = ", ".join([f"{col} = ?" for col in columns])

        # Construct the SQL UPDATE query
        update_query = f"""
        UPDATE {table_name}
        SET {set_clause}
        WHERE {pk} = ?;
        """

        # Prepare the values to be updated
        values = row[columns].tolist() + [df_id]
        
        print("Update query:", update_query)
        print("Values to be updated:", values)
        
        # Execute the update query
        cursor.execute(update_query, values)
        
        # Commit the transaction
        conn.commit()

# DELETE statements
def delete_senior(reference_code):
    referencecode = int(reference_code)
    with make_connection() as conn:
        cursor = conn.cursor()
        # Delete related records in other tables
        cursor.execute("DELETE FROM dependent WHERE referencecode = ?", (referencecode,))
        cursor.execute("DELETE FROM education WHERE referencecode = ?", (referencecode,))
        cursor.execute("DELETE FROM healthconcern WHERE referencecode = ?", (referencecode,))
        cursor.execute("DELETE FROM income WHERE referencecode = ?", (referencecode,))
        
        # Delete senior itself
        cursor.execute("DELETE FROM senior WHERE ReferenceCode = ?", (referencecode, ))
        conn.commit()

def delete_record(table, tbl_pk):
    table_pk_mapping = {
        "dependent": "DepID",
        "education": "EducID",
        "income": "IncomeID",
        "healthconcern": "ConcernID",
        "school": "SchoolID"
    }
    tbl_pk = int(tbl_pk)
    col_name = table_pk_mapping.get(table)
    with make_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table} WHERE {col_name} = ?", (tbl_pk, ))
        conn.commit()