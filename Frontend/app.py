import streamlit as st

from components.templates.inventory_page import inventory_page
from Backend.services.producto_service import listar_productos

st.set_page_config(page_title="Sam's Ferreteria", layout="wide")

st.sidebar.title("Menú")
menu = st.sidebar.radio("Navegación", ["Inventario", "Ventas", "Reportes"])


if menu == "Inventario":
    
    inventory_page()
    
elif menu == "Ventas":
    
    st.title("Registrar Venta")
    st.write("Página de Ventas en construcción... 🛠️")
    
elif menu == "Reportes":
    
    st.title("Reportes")
    st.write("Página de Reportes en construcción... 🛠️")