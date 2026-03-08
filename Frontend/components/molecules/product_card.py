import streamlit as st
from components.atoms.button import primary_button

def product_card(nombre, precio, stock, idx):
    
    st.write(f"**{nombre}** - ${precio} - Stock: {stock}")
    primary_button(f"Comprar {nombre}", key=f"btn_producto_{idx}")