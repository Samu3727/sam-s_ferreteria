from Backend.database.database import get_connection
from Backend.config.settings import DB_CONFIG

__all__ = ["get_connection", "DB_CONFIG"]