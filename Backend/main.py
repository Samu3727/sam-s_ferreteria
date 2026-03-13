from Backend.database.database import get_connection
from Backend.services.producto_service import listar_productos, agregar_producto
from Backend.services.usuarios_service import listar_usuarios, agregar_usuario
from Backend.models.producto import Producto
from Backend.models.usuarios import Usuario

def test_backend():
    
    conn = get_connection()
    print("Conexión exitosa a la base de datos", conn.is_connected)
    conn.close()
    
    productos = listar_productos()
    print("Stock Actual en la ferreteria: ")
    
    
    usuarios = listar_usuarios()
    print("Usuario registrados en el sistema.")
    
    for p in productos:
        print(p)
        
    for u in usuarios:
        print(u)
        

if __name__ == "__main__":
    test_backend()