import streamlit as st
from components.organism.proveedores_table import proveedores_table

def proveedores_page():
    
    st.title("🛻 Proveedores")
    proveedores_table()