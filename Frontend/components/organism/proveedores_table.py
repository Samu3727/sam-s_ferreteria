import streamlit as st
from Backend.services import proveedores_service
from Backend.models.usuarios import Proveedor

def proveedores_table():
    
    if "proveedor_en_edicion" not in st.session_state:
        
        st.session_state.proveedor_en_edicion = None