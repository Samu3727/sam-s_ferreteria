import streamlit as st
from Backend.models.usuarios import Usuario
from Backend.services import usuarios_service

def usuario_nuevo():
    
    st.header("Agregar Usuario.")
    
    if "procesando" not in st.session_state:
        
        st.session_state.procesando = False
        
    if "form_counter" not in st.session_state:
        
        st.session_state.form_counter = 0
        
    with st.form(f"form_agregar_usuario_{st.session_state.form_counter}"):
        
        nombre = st.text_input("Nombre:", placeholder="Nombre del Usuario")
        correo = st.text_input("Correo:", placeholder="pepito123@example.com")
        contrasena = st.text_input("Contraseña", placeholder="*********")
        imagen = st.file_uploader("Imagen:")
        
        enviado = st.form_submit_button("Agregar Usuario", disabled=st.session_state.procesando)
        
        if enviado:
            
            st.session_state.procesando = True
            if not nombre.strip():
                
                st.session_state.procesando = False
                st.warning("El campo de nombre es obligatorio. ⚠️")
                return
            
            
            try:
                
                imagen_bytes = imagen.read() if imagen else None
                usuario = Usuario(nombre=nombre.strip(), correo=correo, contrasena=contrasena)
                usuarios_service.agregar_usuario(usuario)
                st.success(f"Usuario '{nombre}' agregado exitosamente. ✅")
                st.session_state.procesando = False
                st.session_state.form_counter += 1
                st.session_state.mostrar_agregar = False
                st.rerun()
                
            except Exception as e:
                
                st.session_state.procesando = False
                st.error(f"Error al agregar usuario: {e}")
                st.session_state.procesando = False
                
            st.rerun()