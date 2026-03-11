import streamlit as st
from Backend.models.producto import Producto
from Backend.services import producto_service

def producto_nuevo():
    
    st.header("Agregar Producto")
    
    if "procesando" not in st.session_state:
        st.session_state.procesando = False
    
    if "form_counter" not in st.session_state:
        st.session_state.form_counter = 0
    
    with st.form(f"form_agregar_producto_{st.session_state.form_counter}"):
        
        nombre = st.text_input("Nombre:", placeholder="Nombre Producto")
        precio = st.number_input("Precio:")
        stock = st.number_input("Stock:")
        
        enviado = st.form_submit_button("Agregar Producto", disabled=st.session_state.procesando)
        
        if enviado:
            
            st.session_state.procesando = True
            if not nombre.strip():
                st.session_state.procesando = False
                st.warning("El campo de nombre es obligatorio. ⚠️")
                return
            
            try:
                producto = Producto(nombre=nombre.strip(), precio=precio, stock=stock)
                producto_service.agregar_producto(producto)
                st.success(f"✅ Producto '{nombre}' agregado correctamente.")
                st.session_state.procesando = False
                st.session_state.form_counter += 1  # Cambia el key del form
                st.rerun()  # Recarga la página para mostrar el nuevo producto
            except Exception as e:
                st.session_state.procesando = False
                st.error(f"❌ Error al agregar producto: {e}")
                st.session_state.procesando = False