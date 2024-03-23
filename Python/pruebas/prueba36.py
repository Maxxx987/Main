estudiantes = {}

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")
    asignaturas = input("Ingrese las asignaturas cursadas (separadas por comas): ").split(',')

    estudiantes[nombre] = {'edad': edad, 'asignaturas': asignaturas}
    print(f"Estudiante {nombre} agregado exitosamente.\n")

def buscar_estudiante(nombre):
    if nombre in estudiantes:
        print(f"Información de '{nombre}': {estudiantes[nombre]}")
    else:
        print(f"No se encontró al estudiante con el nombre '{nombre}'.")

def listar_estudiantes():
    print("Lista de estudiantes:")
    for nombre in estudiantes:
        print(nombre)
    print()

def actualizar_estudiante(nombre):
    if nombre in estudiantes:
        print(f"Información actual de '{nombre}': {estudiantes[nombre]}")
        atributo = input("¿Qué atributo desea modificar (edad/asignaturas)? ").lower()

        if atributo == 'edad':
            nueva_edad = input("Ingrese la nueva edad: ")
            estudiantes[nombre]['edad'] = nueva_edad
        elif atributo == 'asignaturas':
            nuevas_asignaturas = input("Ingrese las nuevas asignaturas (separadas por comas): ").split(',')
            estudiantes[nombre]['asignaturas'] = nuevas_asignaturas
        else:
            print("Atributo no válido. Por favor, elija entre 'edad' y 'asignaturas'.")

        print(f"Información actualizada de '{nombre}': {estudiantes[nombre]}")
    else:
        print(f"No se encontró al estudiante con el nombre '{nombre}'.")

def eliminar_estudiante(nombre):
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante '{nombre}' eliminado correctamente.")
    else:
        print(f"No se encontró al estudiante con el nombre '{nombre}'.")

# Menú interactivo
while True:
    print("\n--- Menú de Estudiantes ---")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Listar estudiantes")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("6. Salir")

    opcion = input("Ingrese el número de la opción que desea realizar: ")

    if opcion == '1':
        agregar_estudiante()
    elif opcion == '2':
        nombre = input("Ingrese el nombre del estudiante que desea buscar: ")
        buscar_estudiante(nombre)
    elif opcion == '3':
        listar_estudiantes()
    elif opcion == '4':
        nombre = input("Ingrese el nombre del estudiante que desea actualizar: ")
        actualizar_estudiante(nombre)
    elif opcion == '5':
        nombre = input("Ingrese el nombre del estudiante que desea eliminar: ")
        eliminar_estudiante(nombre)
    elif opcion == '6':
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 6.")
