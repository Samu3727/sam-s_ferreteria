import streamlit as st
from Backend.services import usuarios_service
from Backend.models.usuarios import Usuario

def users_table():
    
    if "usuario_en_edicion" not in st.session_state:
        
        st.session_state.usuario_en_edicion = None
        
        
    