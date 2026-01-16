# storage.py
# =================================================
# Este archivo gestiona el guardado y la carga
# de la lista de tareas en un archivo JSON.
#
# Funciones a implementar:
#   - guardar_tareas(tareas, archivo="tareas.json")
#   - cargar_tareas(archivo="tareas.json")hola ajdjasdja
#
# PISTA:
#   Usa json.dump() para guardar
#   Usa json.load() para cargar
#
# Si el archivo no existe al cargar, deberías devolver una lista vacía.
# =================================================ç


import json

def guardar_tareas(tareas, archivo="tareas.json"):
    with open(archivo, 'w') as f:
        json.dump(tareas, f)


def cargar_tareas(archivo="tareas.json"):
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []