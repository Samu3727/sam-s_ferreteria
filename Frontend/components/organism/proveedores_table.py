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
        
        for idx, (nombre, correo, persona, celular) in enumerate([3, 2, 2, 2, 2])
        
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
                    
                    
        