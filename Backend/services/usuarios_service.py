from Backend.database.database import get_connection

def listar_usuarios():
    
    conn = get_connection()
    cur