import json
import os

# Definimos el nombre del archivo donde guardaremos todo. 
FILE_NAME = 'tasks.json'

# --- FUNCIONES AUXILIARES (HELPERS) ---
# El guion bajo '_' al principio del nombre indica que son funciones de uso interno.
# No deben ser llamadas desde el menú de main.py, solo por otras funciones de este mismo archivo.

def _leer_tareas():
    """Lee el archivo JSON y devuelve la lista de tareas. Si no existe, devuelve una lista vacía."""
    
    # 1. Verificamos si el archivo físico 'tasks.json' ya existe en nuestra computadora.
    if not os.path.exists(FILE_NAME):
        # Si no existe (es la primera vez que abrimos el programa), devolvemos una lista vacía.
        return []
    
    # 2. Si el archivo existe, lo abrimos en modo lectura.
    with open(FILE_NAME, 'r') as file:
        try:
            # Intentamos traducir el texto del archivo a una lista de Python usando json.load()
            return json.load(file)
        except json.JSONDecodeError:
            # Si el archivo existe pero está vacío o el texto está roto, 
            # evitamos que el programa explote y devolvemos una lista vacía para empezar de cero.
            return []

def _guardar_tareas(tareas):
    """Recibe una lista de tareas y la sobrescribe en el archivo JSON."""
    
    # Abrimos el archivo en modo escritura. 
    # OJO: El modo 'w' borra todo lo que había antes y escribe lo nuevo por encima.
    with open(FILE_NAME, 'w') as file:
        # Traducimos la lista de Python a formato JSON y la guardamos en el archivo.
        # 'indent=4' hace que el archivo JSON sea con saltos de línea y espacios).
        json.dump(tareas, file, indent=4)

# --- FUNCIONES PRINCIPALES (FEATURES) ---
# Estas son las funciones que sí llamaremos desde nuestro menú en main.py

def create_task():
    # 1. Solicitamos el dato al usuario, dándole una vía de escape.
    titulo = input("Ingresa la descripción de la nueva tarea (o presiona Enter sin escribir nada para cancelar): ")
    
    # 2. .strip() quita los espacios en blanco accidentales. 
    # Si queda vacío (""), significa que el usuario presionó Enter sin texto válido.
    if titulo.strip() == "":
        print("\n❌ Operación cancelada. Volviendo al menú principal...")
        # 'return' aborta la función inmediatamente. El código de abajo no se ejecuta.
        return
    
    # 3. Usamos nuestro helper interno para traer las tareas que ya existen en el archivo.
    tareas = _leer_tareas()

    # 4. Lógica para generar un ID único para la nueva tarea.
    if len(tareas) > 0:
        # Si ya hay tareas, buscamos la última tarea de la lista (tareas[-1]), 
        # miramos qué "id" tiene, y le sumamos 1.
        nuevo_id = tareas[-1]["id"] + 1
    else:
        # Si la lista está vacía (len es 0), el primer ID será 1.
        nuevo_id = 1

    # 5. Estructuramos la nueva tarea como un diccionario.
    nueva_tarea = {
        "id": nuevo_id,          # El ID calculado arriba
        "titulo": titulo,        # El texto que escribió el usuario
        "completada": False      # Por defecto, toda tarea nueva nace sin completar
    }
    
    # 6. Añadimos el nuevo diccionario al final de nuestra lista de tareas.
    tareas.append(nueva_tarea)
    
    # 7. Usamos nuestro otro helper para sobrescribir el archivo JSON con la lista actualizada.
    _guardar_tareas(tareas)
        
    # 8. Damos feedback visual de éxito al usuario.
    print(f"\n✅ Tarea '{titulo}' guardada con éxito.")

def list_tasks():
    """Muestra todas las tareas guardadas en el archivo JSON."""
    
    # 1. Leemos la lista de tareas desde el archivo.
    tareas = _leer_tareas()
    
    # 2. Verificamos si la lista está vacía.
    if len(tareas) == 0:
        print("\n📭 No hay tareas guardadas.")
        return
    
    # 3. Si hay tareas, las mostramos en un formato amigable.
    print("\n📋 Lista de Tareas:")
    for tarea in tareas:
        estado = "✅ Completada" if tarea["completada"] else "❌ Pendiente"
        print(f"ID: {tarea['id']} | {tarea['titulo']} | Estado: {estado}")

def mark_task_completed():
    """Marca una tarea como completada según su ID."""
    
    # 1. Leemos la lista de tareas desde el archivo.
    tareas = _leer_tareas()
    
    # 2. Verificamos si hay tareas para marcar.
    if len(tareas) == 0:
        print("\n📭 No hay tareas guardadas para marcar como completadas.")
        return
    
    # 3. Mostramos las tareas actuales para que el usuario pueda elegir.
    list_tasks()
    
    # 4. Bucle infinito para validar el ingreso del ID
    while True:
        entrada = input("\nIngresa el ID de la tarea que deseas marcar como completada (o Enter para cancelar): ")
        
        # Vía de escape por si el usuario se arrepiente
        if entrada.strip() == "":
            print("\n❌ Operación cancelada. Volviendo al menú principal...")
            return
            
        # Intentamos convertir la entrada a número
        try:
            id_tarea = int(entrada)
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa solo números. Inténtalo de nuevo.")
            continue  # 'continue' hace que el bucle vuelva a empezar desde arriba
            
        # 5. Si es un número válido, buscamos la tarea por su ID
        tarea_encontrada = False
        for tarea in tareas:
            if tarea["id"] == id_tarea:
                tarea_encontrada = True
                
                # Verificamos si ya estaba completada
                if tarea["completada"]:
                    print(f"\n⚠️ La tarea '{tarea['titulo']}' ya está marcada como completada.")
                else:
                    tarea["completada"] = True
                    _guardar_tareas(tareas)
                    print(f"\n✅ Tarea '{tarea['titulo']}' marcada como completada.")
                
                return  # 'return' finaliza la función entera exitosamente
        
        # 6. Si el bucle 'for' terminó y no se encontró la tarea
        if not tarea_encontrada:
            print(f"❌ No se encontró ninguna tarea con el ID {id_tarea}. Inténtalo de nuevo.")
            # Al no haber 'return' ni 'break' aquí, el 'while True' vuelve a empezar