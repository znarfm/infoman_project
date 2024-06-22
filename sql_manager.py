import streamlit as st


def make_connection(name, type):
    return st.connection(name=name, type=type)

# used for viewing all columns from a specific table
def show_table(conn, table_name):
    return conn.query(f"""SELECT * 
                    FROM {table_name};""", ttl=600)


def search_senior(conn, search):
    return conn.query(f"""SELECT name, referencecode 
                      FROM senior 
                      WHERE name LIKE '%{search}%' 
                      ORDER BY name;""", ttl=600)
