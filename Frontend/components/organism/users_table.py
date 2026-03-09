import streamlit as st
from Backend.services import usuarios_service
from Backend.models.usuarios import Usuario

def users_table():
    
    if "usuario_en_edicion" not in st.session_state:
        
        st.session_state.usuario_en_edicion = None
        
        
    st.subheader("👥 Nuestro Usuarios.")
    
    usuarios = usuarios_service.listar_usuarios()
    
    if usuarios:
        
        col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 2, 2])
        
        with col1: st.markdown("**Nombre**")
        with col2: st.markdown("**Correo**")
        with col3: st.markdown("**Contraseña**")
        with col4: st.markdown("**Eliminar**")
        with col5: st.markdown("**Actualizar**")