# src/db/connection.py
import sqlite3
from sqlite3 import Error

def create_connection(db_path):
    """
    Creates a connection to a SQLite database.
    
    Parameters
    ----------
    db_path: str 
        The file path to the SQLite database.
    
    Returns
    -------
    connection: sqlite3.Connection.
        The database connection object, or None if failed.
    """
    connection = None
    try:
        connection = sqlite3.connect(db_path)
        print(f"Connected to SQLite database at: {db_path}")
    except Error as e:
        print(f"SQLite connection error: {e}")

    return connection