import mysql.connector
from Backend.config.settings import DB_CONFIG

def get_connection():
    
    return mysql.connector.connect(**DB_CONFIG)