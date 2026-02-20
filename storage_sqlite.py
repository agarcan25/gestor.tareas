import sqlite3
import os

DATABASE_FILE = "tareas.db"

def crear_bbdd():
    """
    Crea la base de datos SQLite y la tabla de tareas si no existe.
    """
    conexion = sqlite3.connect(DATABASE_FILE)
    cursor = conexion.cursor()

    # Crear tabla de tareas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT NOT NULL,
            prioridad INTEGER,
            completada BOOLEAN DEFAULT 0
        )
    """)

    conexion.commit()
    conexion.close()
    print(F"Base de datos'{DATABASE_FILE}' creada/verificada correctamente.")

def conectar_bbdd():
    """
    Conecta a la base de dator SQLite.
    Retorna la conexión,
    """
    conexion = sqlite3.connect(DATABASE_FILE)
    conexion_row_factory= 