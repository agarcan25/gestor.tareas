import sqlite3
import os

DATABASE_FILE = "tareas.db"


def crear_bbdd():
    conexion = sqlite3.connect(DATABASE_FILE)
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT NOT NULL,
            prioridad INTEGER NOT NULL,
            completada INTEGER DEFAULT 0,
            fecha_creacion TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conexion.commit()
    conexion.close()


def obtener_conexion():
    if not os.path.exists(DATABASE_FILE):
        crear_bbdd()

    conexion = sqlite3.connect(DATABASE_FILE)
    conexion.row_factory = sqlite3.Row
    return conexion


# ===============================
# FUNCIONES
# ===============================

def añadir_tarea(descripcion, prioridad):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO tareas (descripcion, prioridad, completada)
        VALUES (?, ?, 0)
    """, (descripcion, prioridad))

    conexion.commit()
    conexion.close()


def obtener_todas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM tareas ORDER BY prioridad DESC")
    tareas = cursor.fetchall()

    conexion.close()
    return tareas


def obtener_pendientes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM tareas
        WHERE completada = 0
        ORDER BY prioridad DESC
    """)
    tareas = cursor.fetchall()

    conexion.close()
    return tareas


def obtener_completadas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM tareas
        WHERE completada = 1
        ORDER BY prioridad DESC
    """)
    tareas = cursor.fetchall()

    conexion.close()
    return tareas


def marcar_completada(id_tarea):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE tareas
        SET completada = 1
        WHERE id = ?
    """, (id_tarea,))

    conexion.commit()
    conexion.close()


def eliminar_tarea(id_tarea):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM tareas WHERE id = ?", (id_tarea,))

    conexion.commit()
    conexion.close()


# Crear BD al importar
crear_bbdd()