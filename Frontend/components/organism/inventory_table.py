import streamlit as st
from Backend.services import producto_service
from components.molecules.agregarProducto import producto_nuevo
from PIL import Image, UnidentifiedImageError
import io


def _mostrar_imagen_segura(imagen):
    if imagen is None:
        st.write("Sin Imagen")
        return

    if isinstance(imagen, (bytes, bytearray, memoryview)):
        datos = bytes(imagen)
        if not datos:
            st.write("Sin imagen")
            return

        try:
            # Verify bytes are a real image before asking Streamlit to render them.
            Image.open(io.BytesIO(datos)).verify()
            st.image(datos)
        except (UnidentifiedImageError, OSError, ValueError, TypeError):
            st.write("Sin imagen")
        return

    try:
        st.image(imagen)
    except (UnidentifiedImageError, OSError, ValueError, TypeError):
        st.write("Sin imagen")

def inventory_table():
    if "producto_en_edicion" not in st.session_state:
        st.session_state.producto_en_edicion = None
    
    st.subheader("Tabla:")
    
    if "mostrar_agregar" not in st.session_state:
        
        st.session_state.mostrar_agregar = False
    
    if st.session_state.mostrar_agregar:
        producto_nuevo()
        return

    if st.button("Agregar Producto"):
        st.session_state.mostrar_agregar = True
        st.rerun()
    
    productos = producto_service.listar_productos()
    
    if productos:
        col1, col2, col3, col4, col5, col6 = st.columns([3, 2, 2, 2, 2, 2])
        
        with col1: st.markdown("**Imagen**")
        with col2: st.markdown("**Nombre**")
        with col3: st.markdown("**Precio**")
        with col4: st.markdown("**Stock**")
        with col5: st.markdown("**Eliminar**")
        with col6: st.markdown("**Actualizar**")    
        
        for idx, (nombre, precio, stock, imagen) in enumerate(productos):
            
            col1, col2, col3, col4, col5, col6 = st.columns([3, 2, 2, 2, 2, 2])
            
            with col1:
                _mostrar_imagen_segura(imagen)
            with col2: st.write(nombre)
            with col3: st.write(precio)
            with col4: st.write(stock)
            
            with col5:
                
                if st.button("Eliminar🗑️", key=f"eliminar_{idx}"):
                    
                    filas = producto_service.eliminar_producto(nombre, float(precio), int(stock), imagen)
                    
                    if filas > 0:
                        
                        st.success(f"Producto '{nombre}' eliminado exitosamente.✅")
                        st.rerun()
                        
            with col6:
                
                if st.button("Actualizar✏️", key=f"actualizar_{idx}"):
                    st.session_state.producto_en_edicion = {
                        "nombre": nombre,
                        "precio": float(precio),
                        "stock": int(stock),
                        "imagen": imagen
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
                
                st.write(f"Imagen actual: {producto['imagen']}")
                nuevo_imagen = st.file_uploader("Nueva Imagen (opcional):")

                guardar = st.form_submit_button("Guardar Cambios")
                cancelar = st.form_submit_button("Cancelar")

                if guardar:
                    if not nuevo_nombre.strip():
                        st.warning("El nombre no puede estar vacio. ⚠️")
                    else:
                        imagen_bytes = nuevo_imagen.read() if nuevo_imagen else producto["imagen"]
                        filas = producto_service.actualizar_producto(
                            producto["nombre"],
                            float(producto["precio"]),
                            int(producto["stock"]),
                            producto["imagen"],
                            nuevo_nombre.strip(),
                            float(nuevo_precio),
                            int(nuevo_stock),
                            imagen_bytes
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