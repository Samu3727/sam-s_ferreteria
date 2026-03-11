import streamlit as st
from Backend.services import proveedores_service
from Backend.models.usuarios import Proveedor

def proveedores_table():
    
    if "proveedor_en_edicion" not in st.session_state:
        
        st.session_state.proveedor_en_edicion = None
        
        
    st.subheader("Tabla:")
    
    proveedores = proveedores_service.listar_proveedores()
    
    if proveedores:
        
        col1, col2, col3, col4, col5, col6 = st.columns([3, 2, 2, 2, 2])
        
        
        with col1: st.markdown("**Nombre**")
        with col2: st.markdown("**Correo**")
        with col3: st.markdown("**Persona**")
        with col4: st.markdown("**Celular**")
        with col5: st.markdown("Eliminar**")
        with col6: st.markdown("**Actualizar**")
        
        for idx, (nombre, correo, persona, celular) in enumerate(proveedores):
            
            col1, col2, col3, col4, col5, col6 = st.columns("3, 2, 2, 2, 2")
        
            with col1: st.write(nombre)
            with col2: st.write(correo)
            with col3: st.write(persona)
            with col4: st.write(celular)
            
            
            with col5:
                
                if st.button("Eliminar🗑️", key=f"eliminar_{idx}"):
                    
                    filas = proveedores_service.eliminar_proveedor(nombre, correo, persona, celular)
                    
                    if filas > 0:
                        
                        st.success(f"Proveedores '{nombre}' eliminado exitosamente.✅")
                        st.rerun()
                        
                        
            with col6:
                
                if st.button("Actualizar✏️", key=f"actualizar_{idx}"):
                    
                    st.session_state.proveedor_en_edicion = {
                        
                        "nombre": nombre,
                        "correo": correo,
                        "personal": persona,
                        "celular": celular,
                    }
                    
        
        if st.session_state.proveedor_en_edicion:
            
            st.divider()
            st.subheader("Editar Proveedor")
            
            usuario = st.session_state.proveedor_en_edicion
            
            
            with st.form("form_actualizar_proveedor"):
                
                nuevo_nombre = st.text_input("Nombre:", value=proveedor["nombre"])
                nuevo_correo = st.text_input("Correo:", value=proveedor["correo"])
                nuevo_persona = st.text_input("Persona_", value=proveedor["persona"])
                nuevo_celular = st.text_input("Celular:", value=proveedor["celular"])
                
                guardar = st.form_submit_button("Guardar Cambios")
                cancelar = st.form_submit_button("Cancelar")
                
                
                if guardar:
                    
                    if not nuevo_nombre.strip():
                        
                        st.warning("El nombre no puede estar vacio. ⚠️")
                        
                    else:
                        
                        filas = proveedores_service.actualizar_proveedor(
                            
                            proveedor["nombre"],
                            proveedor["correo"],
                            proveedor["persona"],
                            proveedor["celular"],
                            nuevo_nombre.strip(),
                            nuevo_correo,
                            nuevo_persona,
                            nuevo_celular,
                        )
                        
                        if filas > 0:
                            
                            st.success(f"Proveedor '{proveedor['nombre']}' actualizado exitosamente. ✅")
                            st.session_state-proveedor_en_edicion = None
                            st.rerun()
                            
                        else:
                            
                            st.warning("No se puede actualizar el proveedor. ⚠️")
                            
                            
                if cancelar:
                    
                    st.session_state.proveedor_en_edicion = None
                    st.rerun()
                    
    st.divider()
    proveedor_nuevo()
    
    
def proveedor_nuevo():
    
    st.header("Agregar Proveedor.")
    
    if "procesando" not in st.session_state:
        
        st.session_state.procesando = False
        
    if "form_counter" not in st.session_state:
        
        st.session_state.form_counter = 0
        
        
    with st.form(f"form_agregar_proveedor_{st.session_state.form_counter}"):
        
        nombre = st.text_input("Nombre:", placeholder="Nombre Proveedor")
        correo = st.text_input("Correo:", placeholder="distribuidora@example.com")
        persona = st.text_input("Pesona de Contacto:", placeholder="Miguel Perez")
        celular = st.text_input("Telefono de Contacto:", placeholder="30*-***-****")
        
        enviado = st.form_submit_button("Agreagar Proveedor", disabled=st.session_state.procesando)
        
        if enviado:
            
            st.session_state.procesando = True
            
            if not nombre.strip():
                
                st.session_state.procesando = False
                st.warning("El campo de nombre es obligatorio. ⚠️")
                return
            
            
            try:
                
                proveedor = Proveedor(nombre=nombre.strip(), correo=correo, persona=persona, celular=celular)
                proveedores_service.agregar_proveedor(proveedor)
                st.success(f"Proveedor '{nombre}' agregado exitosamente. ✅")
                st.session_state.procesando = False
                st.session_state.form_counter += 1
                st.rerun()
                
                
            except Exception as e:
                
                st.session_state.procesando = False
                st.error(f"Error al agregar el usuario: {e}")
                st.session_state.procesando = False