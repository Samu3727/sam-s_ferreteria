import streamlit as st

from Frontend.components.templates.inventory_page import inventory_page
from Backend.services.producto_service import listar_productos

st.set_page_config(page_title="Sam's Ferreteria", layout="wide")

st.sidebar.title("Menú")
menu = st.sidebar.radio("Navegación", ["Inventario", "Ventas", "Reportes"])


