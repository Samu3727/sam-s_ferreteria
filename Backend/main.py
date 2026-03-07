from Backend.database.database import get_connection
from Backend.services.producto_service import listar_productos, agregar_producto
from Backend.models.producto import Producto

def test_backend():
    
    conn = get_connection()
    print("Conexión exitosa a la base de datos", conn.is_connected)
    conn.close()
    
    