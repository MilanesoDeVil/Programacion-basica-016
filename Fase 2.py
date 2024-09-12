import datetime

class Tarea:
    """Clase base para representar una tarea."""

    def __init__(self, descripcion: str):
        """
        Inicializa una nueva tarea con una descripción.

        :param descripcion: Descripción de la tarea.
        """
        self.descripcion = descripcion
        self.fecha_creacion = datetime.datetime.now()

    def __str__(self):
        return f"{self.descripcion} (Añadida el {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')})"

class TareaConFechaLimite(Tarea):
    """Clase derivada para representar una tarea con fecha límite."""

    def __init__(self, descripcion: str, fecha_limite: datetime.datetime):
        """
        Inicializa una nueva tarea con una fecha límite.

        :param descripcion: Descripción de la tarea.
        :param fecha_limite: Fecha límite para completar la tarea.
        """
        super().__init__(descripcion)
        self.fecha_limite = fecha_limite

    def __str__(self):
        return f"{self.descripcion} (Añadida el {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}, " \
               f"Fecha límite: {self.fecha_limite.strftime('%Y-%m-%d %H:%M:%S')})"

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Menú de Gestión de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Modificar tarea")
    print("5. Salir")

def agregar_tarea(tareas: list, categorias: dict, etiquetas: set):
    """Permite al usuario agregar una nueva tarea a la lista.
    
    :param tareas: Lista donde se almacenan las tareas.
    :param categorias: Diccionario que agrupa tareas por categorías.
    :param etiquetas: Conjunto de etiquetas asociadas a las tareas.
    """
    descripcion = input("Ingrese el nombre de la tarea: ")
    fecha_limite_input = input("Ingrese la fecha límite (YYYY-MM-DD HH:MM:SS) o presione Enter si no tiene: ")
    
    if fecha_limite_input:
        fecha_limite = datetime.datetime.strptime(fecha_limite_input, "%Y-%m-%d %H:%M:%S")
        tarea = TareaConFechaLimite(descripcion, fecha_limite)
    else:
        tarea = Tarea(descripcion)

    tareas.append(tarea)
    print(f"Tarea '{tarea.descripcion}' añadida con éxito.")

def ver_tareas(tareas: list):
    """Muestra todas las tareas almacenadas en la lista.
    
    :param tareas: Lista donde se almacenan las tareas.
    """
    if not tareas:
        print("No hay tareas en la lista.")
    else:
        print("\n--- Lista de Tareas ---")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def eliminar_tarea(tareas: list):
    """Permite al usuario eliminar una tarea de la lista.
    
    :param tareas: Lista donde se almacenan las tareas.
    """
    ver_tareas(tareas)
    if tareas:
        try:
            indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
            if 0 <= indice < len(tareas):
                tarea_eliminada = tareas.pop(indice)
                print(f"Tarea '{tarea_eliminada.descripcion}' eliminada con éxito.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def modificar_tarea(tareas: list):
    """Permite al usuario modificar una tarea existente.
    
    :param tareas: Lista donde se almacenan las tareas.
    """
    ver_tareas(tareas)
    if tareas:
        try:
            indice = int(input("Ingrese el número de la tarea que desea modificar: ")) - 1
            if 0 <= indice < len(tareas):
                nueva_descripcion = input("Ingrese la nueva descripción de la tarea: ")
                tarea = tareas[indice]
                tarea.descripcion = nueva_descripcion
                print(f"Tarea modificada a '{tarea.descripcion}'.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    """Función principal que ejecuta el programa de gestión de tareas."""
    tareas = []
    categorias = {}  # Diccionario para agrupar tareas por categorías (no usado en este ejemplo)
    etiquetas = set()  # Conjunto para almacenar etiquetas (no usado en este ejemplo)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_tarea(tareas, categorias, etiquetas)
        elif opcion == '2':
            ver_tareas(tareas)
        elif opcion == '3':
            eliminar_tarea(tareas)
        elif opcion == '4':
            modificar_tarea(tareas)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor seleccione una opción del menú.")

if __name__ == "__main__":
    main()