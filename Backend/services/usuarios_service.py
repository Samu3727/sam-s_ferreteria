from Backend.database.database import get_connection
from Backend.models.usuarios import Usuario

def listar_usuarios():
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execut("SELECT nombre, correo, contrasena FROM usuarios WHERE estado = 1")
    rows = cursor.fetchall()
    conn.close()
    return rows