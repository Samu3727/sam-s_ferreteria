from Backend.database.database import get_connection
from Backend.models.usuarios import Usuario

def listar_usuarios():
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, correo, contrasena, imagen FROM usuarios WHERE estado = 1")
    rows = cursor.fetchall()
    conn.close()
    return rows


def agregar_usuario(usuario: Usuario):
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, correo, contrasena, imagen) VALUES (%s, %s, %s, %s)",
                    (usuario.nombre, usuario.correo, usuario.contrasena, usuario.imagen))
    
    conn.commit()
    conn.close()
    
    
def eliminar_usuario(nombre: str, correo: str, contrasena: str, imagen: str):
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET estado = 0 WHERE nombre = %s AND correo = %s AND contrasena = %s AND imagen = %s AND estado = 1 LIMIT 1", (nombre, correo, contrasena, imagen))
    
    conn.commit()
    filas_afectadas = cursor.rowcount
    conn.close()
    return filas_afectadas


def actualizar_usuario(nombre: str, nuevo_nombre: str, nuevo_correo: str, nuevo_contrasena: str, nuevo_imagen: str):
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET nombre = %s, correo = %s, contrasena = %s, imagen = %s WHERE nombre = %s AND estado = 1 LIMIT 1", (nuevo_nombre, nuevo_correo, nuevo_contrasena, nuevo_imagen, nombre))
    
    conn.commit()
    filas_afectadas = cursor.rowcount
    conn.close()
    return filas_afectadas