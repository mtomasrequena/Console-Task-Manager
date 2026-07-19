from tasks import create_task, delete_task, list_tasks, mark_task_completed

def main():
    while True:
        print("\n--- Gestor de Tareas de Consola ---")
        print("1. Crear una nueva tarea")
        print("2. Listar todas las tareas")
        print("3. Marcar una tarea como completada")
        print("4. Eliminar una tarea")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == '1':
            create_task()
        elif opcion == '2':
            list_tasks()
        elif opcion == '3':
            mark_task_completed()
        elif opcion == '4':
            delete_task()  # Asegúrate de que esta función esté definida en tasks.py
        elif opcion == '5':
            print("Saliendo del Gestor de Tareas. ¡Hasta luego!")
            break
        else:
            print(">> Opción inválida. Por favor, elige un número del 1 al 5.")

if __name__ == "__main__":
    main()