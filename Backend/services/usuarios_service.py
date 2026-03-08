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
    
    
def eliminar_usuario(nombre: str, correo: str, contrasena: str):
    
    conn = get_connection()
    cursor = conn.sursor()
    cursor.execute("UPDATE usuarios SET estado = 0 WHERE nombre = %s AND correo = %s AND contrasena = %s AND estado = 1 LIMIT 1", (nombre, correo, contrasena))
    
    conn.commit()
    filas_afectadas = cursor.rowcount
    conn.close()
    return filas_afectadas