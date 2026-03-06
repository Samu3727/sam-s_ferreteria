from Backend.database.database import get_connection
from Backend.models.producto import Producto

def listar_productos():
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, precio, stock FROM productos")
    rows = cursor.fetchall()
    conn.close()
    return rows