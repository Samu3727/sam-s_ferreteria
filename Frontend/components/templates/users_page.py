import streamlit as st
from components.organism.users_table import users_table

def users_page():

    st.title("Usuarios de nuestra compañia")
    users_table()