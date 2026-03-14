import streamlit as st
from Backend.services import usuarios_service
from components.molecules.agregarUsuario import usuario_nuevo
from PIL import Image, UnidentifiedImageError
import io

def __mostrar_imagen_segur(imagen):
    
    if imagen is None:
        
        st.write("Sin Imagen")
        return
    
    if isinstance(imagen, (bytes, bytearray, memoryview)):
     
        datos = bytes(imagen)
        
        if not datos:
            
            st.write("Sin Imagen")
            return
        
        try:
            
            Image.open(io.BytesIO(datos)).verify()
            st.imagen(datos)
            
        except (UnidentifiedImageError, OSError, ValueError, TypeError):
            
            st.write("Sin IMagen")
            return
    
def users_table():
    
    if "usuario_en_edicion" not in st.session_state:
        
        st.session_state.usuario_en_edicion = None
        
        
    st.subheader("Tabla:")
    
    if "mostrar_agregar" not in st.session_state:
        
        st.session_state.mostrar_agregar = False
        
    if st.session_state.mostrar_agregar:
        usuario_nuevo()
        return
    
    if st.button("Agregar Usuario"):
        
        st.session_state.mostrar_agregar = True
        st.rerun()
    
    usuarios = usuarios_service.listar_usuarios()
    
    if usuarios:
        
        col1, col2, col3, col4, col5, col6 = st.columns([3, 2, 2, 2, 2, 2])
        
        with col1: st.markdown("**Imagen**")
        with col2: st.markdown("**Nombre**")
        with col3: st.markdown("**Correo**")
        with col4: st.markdown("**Contraseña**")
        with col5: st.markdown("**Eliminar**")
        with col6: st.markdown("**Actualizar**")
        
        for idx, (nombre, correo, contrasena, imagen) in enumerate(usuarios):
            
            col1, col2, col3, col4, col5, col6 = st.columns([3, 2, 2, 2, 2, 2])
            
            with col1: st.write(imagen) if imagen else st.write("Sin imagen")
            with col2: st.write(nombre)
            with col3: st.write(correo)
            with col4: st.write(contrasena)
            
            
            with col5:
                
                if st.button("Eliminar🗑️", key=f"eliminar_{idx}"):
                    
                    filas = usuarios_service.eliminar_usuario(nombre, correo, contrasena, imagen)
                    
                    if filas > 0:
                        
                        st.success(f"Usuario '{nombre}' eliminado exitosamente.✅")
                        st.rerun()
                        
                        
            with col6:
                
                if st.button("Actualizar✏️", key=f"actualizar_{idx}"):
                    st.session_state.usuario_en_edicion = {
                        "nombre": nombre,
                        "correo": correo,
                        "contrasena": contrasena,
                        "imagen": imagen
                    }
                    
                    
                    
        if st.session_state.usuario_en_edicion:
            
            st.divider()
            st.subheader("Editar Usuario")
            
            
            usuario = st.session_state.usuario_en_edicion
            
            with st.form("form_actualizar_usuario"):
                
                nuevo_nombre = st.text_input("Nombre:", value=usuario["nombre"])
                nuevo_correo = st.text_input("Correo:", value=usuario["correo"])
                nuevo_contrasena = st.text_input("Contraseña:", value=usuario["contrasena"])
                
                st.write(f"Imagen actual: {usuario['imagen']}")
                nuevo_imagen = st.file_uploader("Nueva Imagen (Opcional):")
                
                guardar = st.form_submit_button("Guardar Cambios")
                cancelar = st.form_submit_button("Cancelar")
                
                
                if guardar:
                    
                    if not nuevo_nombre.strip():
                        
                        st.warning("El nombre no puede estar vacio. ⚠️")
                        
                    else:
                        
                        imagen_bytes = nuevo_imagen.read() if nuevo_imagen else usuario["imagen"]
                        filas = usuarios_service.actualizar_usuario(
                            
                            usuario["nombre"],
                            nuevo_nombre.strip(),
                            nuevo_correo,
                            nuevo_contrasena,
                            imagen_bytes
                        )
                        
                        
                        if filas > 0:
                            
                            st.success(f"Usuario '{usuario['nombre']}' actualizado exitosamente.✅")
                            st.session_state.usuario_en_edicion = None
                            st.rerun()
                            
                        else:
                            
                            st.warning("No se pudo actualizar el usuario. ⚠️")
                            
                            
                if cancelar:
                    
                    st.session_state.usuario_en_edicion = None
                    st.rerun()
                    
                    
    st.divider()