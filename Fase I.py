import datetime

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Menú de Gestión de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

def agregar_tarea(tareas):
    """Permite al usuario agregar una nueva tarea a la lista."""
    tarea = input("Ingrese el nombre de la tarea: ")
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tareas.append({"tarea": tarea, "fecha": fecha_actual})
    print(f"Tarea '{tarea}' añadida con éxito.")

def ver_tareas(tareas):
    """Muestra todas las tareas almacenadas en la lista."""
    if not tareas:
        print("No hay tareas en la lista.")
    else:
        print("\n--- Lista de Tareas ---")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea['tarea']} (Añadida el {tarea['fecha']})")

def eliminar_tarea(tareas):
    """Permite al usuario eliminar una tarea de la lista."""
    ver_tareas(tareas)
    if tareas:
        try:
            indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
            if 0 <= indice < len(tareas):
                tarea_eliminada = tareas.pop(indice)
                print(f"Tarea '{tarea_eliminada['tarea']}' eliminada con éxito.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    """Función principal que ejecuta el programa de gestión de tareas."""
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            ver_tareas(tareas)
        elif opcion == '3':
            eliminar_tarea(tareas)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor seleccione una opción del menú.")

if __name__ == "__main__":
    main()
