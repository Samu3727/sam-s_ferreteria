from Backend.database.database import get_connection
from Backend.models.producto import Producto

def listar_productos():
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, precio, stock, imagen FROM productos WHERE estado = 1")
    rows = cursor.fetchall()
    conn.close()
    return rows

def agregar_producto(producto: Producto):
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio, stock, imagen) VALUES (%s,%s, %s, %s)",
                (producto.nombre, producto.precio, producto.stock, producto.imagen))
    
    conn.commit()
    conn.close()
    
def eliminar_producto(nombre: str, precio: float, stock: int, imagen: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE productos
        SET estado = 0
        WHERE nombre = %s AND precio = %s AND stock = %s AND imagen = %s AND estado = 1
        LIMIT 1
        """,
        (nombre, precio, stock, imagen)
    )
    conn.commit()
    filas_afectadas = cursor.rowcount
    conn.close()
    return filas_afectadas


def actualizar_producto(nombre: str, *args):

    conn = get_connection()
    cursor = conn.cursor()

    if len(args) == 3:
        nuevo_nombre, nuevo_precio, nuevo_stock, nuevo_imagen = args
        cursor.execute(
            """
            UPDATE productos
            SET nombre = %s, precio = %s, stock = %s, imagen = %s
            WHERE nombre = %s AND estado = 1
            LIMIT 1
            """,
            (nuevo_nombre, nuevo_precio, nuevo_stock,nuevo_imagen, nombre),
        )
    elif len(args) == 5:
        precio, stock, imagen, nuevo_nombre, nuevo_precio, nuevo_stock, nuevo_imagen = args
        cursor.execute(
            """
            UPDATE productos
            SET nombre = %s, precio = %s, stock = %s
            WHERE nombre = %s AND precio = %s AND stock = %s AND imagen = %s AND estado = 1
            LIMIT 1
            """,
            (nuevo_nombre, nuevo_precio, nuevo_stock, nuevo_imagen, nombre, precio, stock, imagen),
        )
    else:
        conn.close()
        raise TypeError(
            "actualizar_producto admite 4 o 6 argumentos en total."
        )

    conn.commit()
    filas_afectadas = cursor.rowcount
    conn.close()
    return filas_afectadas