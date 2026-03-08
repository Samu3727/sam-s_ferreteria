from Backend.database.database import get_connection
from Backend.models.usuarios import Usuario

def listar_usuarios():
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execut("SELECT nombre, correo, contrasena FROM usuarios WHERE estado = 1")
    rows = cursor.fetchall()
    conn.close()
    return rows


def agregar_usuario():
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, correo, contrasena) VALUES (%s, %s, %s)",
                    (Usuario.nombre, Usuario.correo, Usuario.contrasena))
    
    conn.commit()
    conn.close()