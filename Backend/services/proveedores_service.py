from Backend.database.database import get_connection
from Backend.models.proveedores import Proveedor

def listar_proveedores():
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, correo, persona, celular FROM proveedores WHERE estado = 1")
    rows = cursor.fetchall()
    conn.close()
    return rows

def agregar_proveedor(proveedor: Proveedor):
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO proveedores (nombre, correo, persona, celular) VALUES (%s, %s, %s, %s)",
                    (proveedor.nombre, proveedor.correo, proveedor.persona, proveedor.celular))
    
    conn.commit()
    conn.close()
    
    
def eliminar_proveedor(nombre: str, correo: str, persona: str, celular: str):
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE proveedores SET estado = 0 WHERE nombre = %s AND correo = %s AND persona = %s AND celular = %s AND estado = 1 LIMIT 1", (nombre, correo, persona, celular))
    
    conn.commit()
    filas_afectadas = cursor.rowcount
    conn.close()
    return filas_afectadas


def actualizar_proveedor(nombre: str, nuevo_nombre: str, nuevo_correo: str, nuevo_persona: str, nuevo_celular: str):
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE proveedores SET nombre = %s, correo = %s, persona = %s, celular = %s WHERE nombre = %s AND estado = 1 LIMIT 1", (nuevo_nombre, nuevo_correo, nuevo_persona, nuevo_celular, nombre))
    
    conn.commit()
    filas_afectadas = cursor.rowcount
    conn.close()
    return filas_afectadas