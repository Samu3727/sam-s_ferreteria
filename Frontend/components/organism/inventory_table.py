import streamlit as st
from components.molecules.product_card import product_card
from Backend.services.producto_service import listar_productos, agregar_producto
from Backend.models.producto import Producto

def inventory_table():
    
    productos = listar_productos()
    
    for nombre, precio, stock in productos:
        
        product_card(nombre, precio, stock)
        
        
    st.divider()
    producto_nuevo()
        
        
def producto_nuevo():
    
    st.header("Agregar Producto")
    
    with st.form("form_agregar_prodcuto"):
        
        nombre = st.text_input("Nombre:", placeholder="Nombre Producto")
        precio = st.number_input("Precio:", min_value=0.0, step=50.0)
        stock = st.number_input("Stock:", min_value=0, step=1)
        
        enviado = st.form_submit_button("Agregar Producto")
        
        if enviado:
            if not nombre.strip():
                
                st.warning("El campo de nombre es obligatorio. ⚠️")
                return
            
            try:
                producto = Producto(nombre=nombre.strip(), precio=precio, stock=stock)
                agregar_producto(producto)
                st.success(f"✅ Producto '{nombre}' agregado correctamente.")
                st.rerun()  # Recarga la página para mostrar el nuevo producto
            except Exception as e:
                st.error(f"❌ Error al agregar producto: {e}")