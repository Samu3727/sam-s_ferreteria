import sys
from pathlib import Path

# Agregar el directorio raíz del proyecto al sys.path
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

import streamlit as st
from components.templates.inventory_page import inventory_page
from components.templates.users_page import users_page

st.set_page_config(page_title="Ferretería App", layout="wide")

st.sidebar.title("Menú")
menu = st.sidebar.radio("Navegación", ["Inventario", "Proveedores", "Usuarios", "Ventas", "Reportes"])

if menu == "Inventario":
    inventory_page()
    
elif menu == "Proveedores":
    st.title("Proveedores")
    st.write("Página de Proveedores en construcción...")

elif menu == "Ventas":
    st.title("Registrar Venta")
    st.write("Formulario de ventas en construcción...")

elif menu == "Reportes":
    st.title("Reportes")
    st.write("Reportes en construcción...")
    
elif menu == "Usuarios":
    users_page()