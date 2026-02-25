# storage_sqlite.py
# =================================================
# Este archivo se encarga de la persistencia de datos usando SQLite.
# Proporciona funciones para crear la base de datos,
# conectarse a ella y realizar operaciones de lectura/escritura.
#
# Funciones a implementar:
#   - crear_bbdd() - Crear la base de datos y tablas si no existen
#   - conectar_bbdd() - Conectar a la base de datos
#   - obtener_conexion() - Obtener conexión activa
#
# IMPORTANTE:
#   Este módulo coexistirá con storage.py (JSON) durante la transición
#   hacia persistencia basada en SQLite.
# =================================================

import sqlite3
import os


DATABASE_FILE = "tareas.db"


def crear_bbdd():
    """
    Crea la base de datos SQLite y la tabla de tareas si no existen.
    """
    conexion = sqlite3.connect(DATABASE_FILE)
    cursor = conexion.cursor()
    
    # Crear tabla de tareas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT NOT NULL,
            prioridad INTEGER,
            completada BOOLEAN DEFAULT 0
        )
    """)
    
    conexion.commit()
    conexion.close()
    print(f"Base de datos '{DATABASE_FILE}' creada/verificada correctamente.")


def conectar_bbdd():
    """
    Conecta a la base de datos SQLite.
    Retorna la conexión.
    """
    conexion = sqlite3.connect(DATABASE_FILE)
    conexion.row_factory = sqlite3.Row  # Permite acceder a columnas por nombre
    return conexion


def obtener_conexion():
    """
    Obtiene una conexión activa a la base de datos.
    Asegura que la BD existe antes de conectar.
    """
    if not os.path.exists(DATABASE_FILE):
        crear_bbdd()
    return conectar_bbdd()


# Inicializar la BD al importar el módulo
if __name__ != "__main__":
    crear_bbdd()