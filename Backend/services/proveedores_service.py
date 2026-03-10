from Backend.database.database import get_connection
from Backend.models.proveedores import Proveedor

def listar_proveedores():
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, correo, persona, celular FROM proveedores WHERE estado = 1")
    rows = cursor.fetchall()
    conn.close()
    return rows