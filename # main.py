from storage_sqlite import (
    añadir_tarea,
    obtener_todas,
    obtener_pendientes,
    obtener_completadas,
    marcar_completada,
    eliminar_tarea
)


def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Añadir tarea")
    print("2. Marcar tarea como completada")
    print("3. Eliminar tarea")
    print("4. Ver tareas pendientes")
    print("5. Ver tareas completadas")
    print("0. Salir")


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: introduce un número entero válido.")


def mostrar_lista(tareas):
    if not tareas:
        print("No hay tareas.")
        return

    for tarea in tareas:
        estado = "✔" if tarea["completada"] else "✘"
        print(f'ID {tarea["id"]} [{estado}] {tarea["descripcion"]} (Prioridad: {tarea["prioridad"]})')


def main():
    
    while True:
        mostrar_menu()
        opcion = pedir_entero("Elige una opción: ")

        if opcion == 1:
            descripcion = input("Descripción: ")
            prioridad = pedir_entero("Prioridad (1-5): ")
            añadir_tarea(descripcion, prioridad)
            print("Tarea añadida correctamente.")

        elif opcion == 2:
            tareas = obtener_todas()
            mostrar_lista(tareas)
            id_tarea = pedir_entero("ID de la tarea a completar: ")
            marcar_completada(id_tarea)
            print("Tarea marcada como completada.")

        elif opcion == 3:
            tareas = obtener_todas()
            mostrar_lista(tareas)
            id_tarea = pedir_entero("ID de la tarea a eliminar: ")
            eliminar_tarea(id_tarea)
            print("Tarea eliminada.")

        elif opcion == 4:
            print("\n--- TAREAS PENDIENTES ---")
            tareas = obtener_pendientes()
            mostrar_lista(tareas)

        elif opcion == 5:
            print("\n--- TAREAS COMPLETADAS ---")
            tareas = obtener_completadas()
            mostrar_lista(tareas)

        elif opcion == 0:
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()