estudiantes = {}

def agregar_estudiante():
    # Implementar la función para agregar un nuevo estudiante al diccionario
    nombre = input('Nombre: ')
    materias = {}
    
    while True:
        materia = input('Materia: ("fin" si desea salir)')
        if materia.lower() == 'fin':
            break
        nota = input('Nota: ')
        materias[materia] = nota
    
    estudiantes[nombre] = materias
        
    

def buscar_estudiante(nombre):
    # Implementar la función para buscar un estudiante por su nombre
    #return estudiantes.get(nombre)

    for k, v in estudiantes.items():
        if nombre in k:
            return v
    print('Estudiante no encontrado')
    None


def listar_estudiantes():
    # Implementar la función para listar todos los estudiantes
    print(estudiantes)

def actualizar_estudiante(nombre):
    # Implementar la función para actualizar la información de un estudiante
    
    print('Que materia desea cambiar?\n',estudiantes[nombre])
    
    while True:
        materia = input('Materia: ("fin" si desea salir)')
        if materia.lower() == 'fin':
            break
        nota = input('Nota: ')
        estudiantes[nombre][materia] = nota
    
    
    
    
    
def eliminar_estudiante(nombre):
    # Implementar la función para eliminar un estudiante del diccionario
    estudiantes.pop(nombre)

# Aquí puedes implementar un menú interactivo para que el usuario realice operaciones



while True:
    print('--------Menu estudiantes-------')
    print('1- Agregar Estudiante')
    print('2- Buscar Estudiante')
    print('3- Listar Estudiantes')
    print('4- Actualizar Estudiante')
    print('5- Eliminar Estudante')
    print('6- Salir')
    
    a = input('Elija un numero:\n')
    
    if a == '1':
        agregar_estudiante()
    elif a == '2':
        nombre = input('Nombre: ')
        print(f'{nombre}: ', buscar_estudiante(nombre))
    elif a == '3':
        listar_estudiantes()
    elif a == '4':
        nombre = input('Nombre: ')
        actualizar_estudiante(nombre)
    elif a == '5':
        nombre = input('Nombre: ')
        eliminar_estudiante(nombre)
    elif a == '6':
        break
    else:
        print('Opcion no valida, elija un numero')
        

























