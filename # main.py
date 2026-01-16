# main.py
# =================================================
# Este archivo se encarga de la interacción con el usuario.
# Aquí NO se gestiona la lógica: eso se hace en models.py.
# Tampoco se guarda/carga directamente: eso lo hace storage.py.
#
# Tareas principales:
#   - Crear el menú
#   - Leer opciones del usuario
#   - Llamar a las funciones de models y storage
#   - Mostrar las tareas por pantalla
#
# Funciones a implementar:
#   - mostrar_menu()
#   - pedir_entero(mensaje)
#   - mostrar_lista(tareas)
#   - main()
#
# IMPORTANTE:
#   main() debe contener el bucle principal
#   que permita al usuario interactuar hasta que elija salir.
# =================================================
# =================================================
# Interacción con el usuario
# =================================================

from models import (
    añadir_tarea,
    marcar_completada,
    eliminar_tarea,
    obtener_tareas_pendientes,
    obtener_tareas_completadas
)

from storage import guardar_tareas, cargar_tareas


def mostrar_menu():
    """
    Muestra el menú principal con las opciones disponibles.
    """
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Añadir tarea")
    print("2. Marcar tarea como completada")
    print("3. Eliminar tarea")
    print("4. Ver tareas pendientes")
    print("5. Ver tareas completadas")
    print("0. Salir")


def pedir_entero(mensaje):
    """
    Pide un número entero.
    Repite hasta que sea válido.
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: introduce un número entero válido.")


def mostrar_lista(tareas):
    """
    Muestra por pantalla las tareas recibidas.
    """
    if not tareas:
        print("No hay tareas para mostrar.")
        return

    for i, tarea in enumerate(tareas):
        estado = "hecho" if tarea.get("completada") else "no hecho"
        print(f"{i}. [{estado}] {tarea.get('titulo')}")


def main():
    """
    Bucle programa.
    """
    tareas = cargar_tareas()
    if tareas is None:
        tareas = []

    while True:
        mostrar_menu()
        opcion = pedir_entero("Elige una opción: ")

        if opcion == 1:
            titulo = input("Introduce el título de la tarea: ")
            añadir_tarea(tareas, titulo)
            guardar_tareas(tareas)
            print(" Tarea añadida correctamente.")

        elif opcion == 2:
            mostrar_lista(tareas)
            indice = pedir_entero("Índice de la tarea a completar: ")
            marcar_completada(tareas, indice)
            guardar_tareas(tareas)
            print("Tarea marcada como completada.")

        elif opcion == 3:
            mostrar_lista(tareas)
            indice = pedir_entero("Índice de la tarea a eliminar: ")
            eliminar_tarea(tareas, indice)
            guardar_tareas(tareas)
            print(" Tarea eliminada.")

        elif opcion == 4:
            print("\n--- TAREAS PENDIENTES ---")
            pendientes = obtener_tareas_pendientes(tareas)
            mostrar_lista(pendientes)

        elif opcion == 5:
            print("\n--- TAREAS COMPLETADAS ---")
            completadas = obtener_tareas_completadas(tareas)
            mostrar_lista(completadas)

        elif opcion == 0:
            guardar_tareas(tareas)
            print(" Saliendo del programa...")
            break

        else:
            print(" Opción no válida.")


# Ejecutar el programa solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    main() 
