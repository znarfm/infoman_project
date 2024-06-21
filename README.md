# Information Management Project

## Overview

We made a senior citizen database application that can do the basic CRUD operations.The application is based on the National Commission of Senior Citizens (NCSC) information form.

## Installation

1. Clone the repository.
2. Create a new virtual environment using `python -m venv venv`.
3. Activate the virtual environment using `.\venv\bin\activate` on Windows or `source venv/bin/activate` on Linux.
4. Install the dependencies using `pip install -r requirements.txt`.
5. Create a .streamlit folder and add a secrets.toml file.
    Add the following information to the file:

    ```toml
    [connections.mysql]

    dialect = "mysql"
    host = "localhost"
    port = 3306
    database = "project"
    username = "<username>"
    password = "<password>"
    query = { charset = 'utf8mb4' }
    ```

6. Run the application using `streamlit run main.py`, and your browser should open automatically.
