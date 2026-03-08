from Backend.database.database import get_connection
from Backend.models.producto import Producto

def listar_productos():
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, precio, stock FROM productos WHERE estado = 1")
    rows = cursor.fetchall()
    conn.close()
    return rows

def agregar_producto(producto: Producto):
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (%s,%s, %s)",
                (producto.nombre, producto.precio, producto.stock))
    
    conn.commit()
    conn.close()
    
def eliminar_producto(nombre: str, precio: float, stock: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE productos
        SET estado = 0
        WHERE nombre = %s AND precio = %s AND stock = %s AND estado = 1
        LIMIT 1
        """,
        (nombre, precio, stock)
    )
    conn.commit()
    filas_afectadas = cursor.rowcount
    conn.close()
    return filas_afectadas

