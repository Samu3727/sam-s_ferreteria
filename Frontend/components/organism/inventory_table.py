import streamlit as st
from Backend.services import producto_service
from components.molecules.agregarProducto import producto_nuevo

def inventory_table():
    if "producto_en_edicion" not in st.session_state:
        st.session_state.producto_en_edicion = None
    
    st.subheader("Tabla:")
    
    if "mostrar_agregar" not in st.session_state:
        
        st.session_state.mostrar_agregar = False
    
    if st.button("Agregar Producto"):
        
        st.session_state.mostrar_agregar = True
        
    if st.session_state.mostrar_agregar:
        producto_nuevo()
    
    productos = producto_service.listar_productos()
    
    if productos:
        col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 2, 2])
        
        with col1: st.markdown("**Nombre**")
        with col2: st.markdown("**Precio**")
        with col3: st.markdown("**Stock**")
        with col4: st.markdown("**Eliminar**")
        with col5: st.markdown("**Actualizar**")    
        
        for idx, (nombre, precio, stock) in enumerate(productos):
            
            col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 2, 2])
            
            with col1: st.write(nombre)
            with col2: st.write(precio)
            with col3: st.write(stock)
            
            with col4:
                
                if st.button("Eliminar🗑️", key=f"eliminar_{idx}"):
                    
                    filas = producto_service.eliminar_producto(nombre, float(precio), int(stock))
                    
                    if filas > 0:
                        
                        st.success(f"Producto '{nombre}' eliminado exitosamente.✅")
                        st.rerun()
                        
            with col5:
                
                if st.button("Actualizar✏️", key=f"actualizar_{idx}"):
                    st.session_state.producto_en_edicion = {
                        "nombre": nombre,
                        "precio": float(precio),
                        "stock": int(stock),
                    }

        if st.session_state.producto_en_edicion:
            st.divider()
            st.subheader("Editar Producto")

            producto = st.session_state.producto_en_edicion

            with st.form("form_actualizar_producto"):
                nuevo_nombre = st.text_input("Nombre:", value=producto["nombre"])
                nuevo_precio = st.number_input(
                    "Precio:",
                    value=float(producto["precio"]),
                    min_value=0.0,
                    step=1.0,
                )
                nuevo_stock = st.number_input(
                    "Stock:",
                    value=int(producto["stock"]),
                    min_value=0,
                    step=1,
                )

                guardar = st.form_submit_button("Guardar Cambios")
                cancelar = st.form_submit_button("Cancelar")

                if guardar:
                    if not nuevo_nombre.strip():
                        st.warning("El nombre no puede estar vacio. ⚠️")
                    else:
                        filas = producto_service.actualizar_producto(
                            producto["nombre"],
                            float(producto["precio"]),
                            int(producto["stock"]),
                            nuevo_nombre.strip(),
                            float(nuevo_precio),
                            int(nuevo_stock),
                        )

                        if filas > 0:
                            st.success(f"Producto '{producto['nombre']}' actualizado exitosamente.✅")
                            st.session_state.producto_en_edicion = None
                            st.rerun()
                        else:
                            st.warning("No se pudo actualizar el producto.⚠️")

                if cancelar:
                    st.session_state.producto_en_edicion = None
                    st.rerun()
                        
    st.divider()