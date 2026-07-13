import json
import os

FILE_NAME = 'tasks.json'

def create_task():
    # 1. Pedir al usuario el nombre de la tarea
    titulo = input("Ingresa la descripción de la nueva tarea (o presiona Enter sin escribir nada para cancelar): ")
    
    if titulo.strip() == "":
        print("\n❌ Operación cancelada. Volviendo al menú principal...")
        return  # Esto finaliza la función inmediatamente
    
    # 2. Leer las tareas existentes (si el archivo ya existe)
    tareas = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            try:
                tareas = json.load(file)
            except json.JSONDecodeError:
                tareas = [] # Si el archivo está vacío o corrupto, empezamos de cero

    # 3. Crear la nueva tarea en formato diccionario
    nueva_tarea = {
        "id": len(tareas) + 1,
        "titulo": titulo,
        "completada": False
    }
    
    # 4. Agregarla a la lista
    tareas.append(nueva_tarea)
    
    # 5. Guardar la lista actualizada en el archivo JSON
    with open(FILE_NAME, 'w') as file:
        json.dump(tareas, file, indent=4)
        
    print(f"\n✅ Tarea '{titulo}' guardada con éxito.")