


estudiantes = {'estudiante1' : {'nombre': 'maxi', 'edad': '28', 'asignaturas': ['matematica', 'lengua', 'geografia']},
               'estudiante2' : {'nombre': 'juan', 'edad': '42', 'asignaturas': ['historia', 'lengua', 'educacion fisica']}}

def agregar_estudiante():
    # Implementar la función para agregar un nuevo estudiante al diccionario
    codigo = f'estudiante{len(estudiantes)+1}'
    nombre = input('Nombre: ')
    edad = input('Edad: ')
    asignaturas = input('Asignaturas (separadas por coma): ').split(',')
    
    estudiantes[codigo] = {'nombre' : nombre, 'edad': edad, 'asignaturas': asignaturas}

def buscar_estudiante(nombre):
    # Implementar la función para buscar un estudiante por su nombre
   
    for estudiante in estudiantes:
        if  nombre in estudiantes[estudiante].values():
            return estudiante
    return None
    



def listar_estudiantes():
    # Implementar la función para listar todos los estudiantes
    for k, v in estudiantes.items():
        print(k, v)

def actualizar_estudiante(nombre):
    # Implementar la función para actualizar la información de un estudiante
    est = buscar_estudiante(nombre)
    print('ESt: ', est)
    
    nombre = input('Nombre: ')
    edad = input('Edad: ')
    asignaturas = input('Asignaturas (separadas por coma): ')
    
    if len(nombre) > 0:
        estudiantes[est]['nombre'] =  nombre
    if len(edad)> 0:
        estudiantes[est]['edad'] = edad
    if len(asignaturas) > 0:
        asignaturas = asignaturas.split(',')
        estudiantes[est]['asignaturas'] = asignaturas
        
        
    
    
    
    

def eliminar_estudiante(nombre):
    # Implementar la función para eliminar un estudiante del diccionario
    est = buscar_estudiante(nombre)
    
    estudiantes.pop(est)
    print('Estudiante eliminado exitosamente')
    

# Aquí puedes implementar un menú interactivo para que el usuario realice operaciones

while True:
    print('-----------Bienvenido!-------------')
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Listar estudiantes")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("6. Salir")
    
    a = input('Elija una opcion:\n')
    
    if a == '1':
        agregar_estudiante()
    elif a == '2':
        nombre = input('Nombre: ')
        print(estudiantes[buscar_estudiante(nombre)])
    elif a == '3':
        listar_estudiantes()
    elif a == '4':
        nombre = input('Nombre: ')
        actualizar_estudiante(nombre)
    elif a == '5':
        nombre = input('Nombre: ')        
        eliminar_estudiante(nombre)
    elif a == '6':
        print('Adios!')
        break
    else:
        print('Numero invalido, elija una de las opciones')
    