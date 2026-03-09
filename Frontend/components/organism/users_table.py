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
        
        for idx, (nombre, correo, contrasena) in enumerate(usuarios):
            
            col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 2, 2])
            
            with col1: st.write(nombre)
            with col2: st.write(correo)
            with col3: st.write(contrasena)
            
            
            with col4:
                
                if st.button("Eliminar🗑️", key=f"eliminar_{idx}"):
                    
                    filas = usuarios_service.eliminar_usuario(nombre, correo, contrasena)
                    
                    if filas > 0:
                        
                        st.success(f"Usuario '{nombre}' eliminado exitosamente.✅")
                        st.rerun()
                        
                        
            with col5:
                
                if st.button("Actualizar✏️", key=f"actualizar_{idx}"):
                    st.session_state.producto_en_edicion = {
                        "nombre": nombre,
                        "correo": correo,
                        "contrasena": contrasena,
                    }
                    
                    
                    
        if st.session_state.usuario_en_edicion:
            
            st.divider()
            st.subheader("Editar Usuario")
            
            
            usuario = st.session_state.usuario_en_edicion
            
            with st.form("form_actualizar_usuario"):
                
                nuevo_nombre = st.text_input("Nombre:", value=usuario["nombre"])
                nuevo_correo = st.text_input("Correo:", value=usuario["correo"])
                nuevo_contrasena = st.text_input("Contraseña:", value=usuario["contrasena"])
                
                guardar = st.form_submit_button("Guardar Cambios")
                cancelar = st.form_submit_button("Cancelar")
                
                
                if guardar:
                    
                    if not nuevo_nombre.strip():
                        
                        st.warning("El nombre no puede estar vacio. ⚠️")
                        
                    else:
                        
                        filas = usuarios_service.actualizar_usuario(
                            
                            usuario["nombre"],
                            usuario["correo"],
                            usuario["contrasena"],
                            nuevo_nombre.strip(),
                            nuevo_correo,
                            nuevo_contrasena,
                        )
                        
                        
                        if filas > 0:
                            
                            st.success(f"Usuario '{usuario['nombre']}' actualizado exitosamente.✅")
                            st.session_state.usuario_en_edicion = None
                            st.rerun()
                            
                        else:
                            
                            st.warning("No se pudo actualizar el producto. ⚠️")
                            
                            
                if cancelar:
                    
                    st.session_state.usuario_en_edicion = None
                    st.rerun()
                    
                    
    st.divider()
    usuario_nuevo()
    
    
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
        
        enviado = st.form_submit_button("Agregar Usuario", disabled=st.session_state.procesando)
        
        if enviado:
            
            st.session_state.procesando = True
            if not nombre.strip():
                
                st.session_state.procesando = False
                st.warning("El campo de nombre es obligatorio. ⚠️")
                return
            
            
            