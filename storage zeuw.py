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