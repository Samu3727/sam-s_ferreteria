import streamlit as st
from components.molecules.product_card import product_card
from Backend.services import listra_productos

def inventory_table():
    
    productos = listra_productos()
    
    for nombre, precio, stock in productos:
        
        product_card(nombre, precio, stock)