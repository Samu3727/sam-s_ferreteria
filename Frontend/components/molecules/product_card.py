import streamlit as st
from components.atoms.button import primary_button

def product_card(nombre, precio, stock):
    
    st.write(f"**{nombre}** - ${precio} - Stock: {stock}")
    primary_button(f"Comprar {nombre}")