from tasks import create_task

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
            print(">> Opción seleccionada: Listar tareas (Lógica pendiente)")
        elif opcion == '3':
            print(">> Opción seleccionada: Completar tarea (Lógica pendiente)")
        elif opcion == '4':
            print(">> Opción seleccionada: Eliminar tarea (Lógica pendiente)")
        elif opcion == '5':
            print("Saliendo del Gestor de Tareas. ¡Hasta luego!")
            break
        else:
            print(">> Opción inválida. Por favor, elige un número del 1 al 5.")

if __name__ == "__main__":
    main()