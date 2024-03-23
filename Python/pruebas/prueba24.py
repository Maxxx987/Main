

registro1 = []

def agregar_estudiante(registro):
    nombre = input('Nombre: ')
    edad = int(input('Edad: '))
    estudiante = {'Nombre': nombre, 'Edad': edad}
    registro.append(estudiante)
    
def mostrar_estudiantes(registro):
    print(registro)


def buscar_estudiante(registro):
    nombre = input('Nombre: ')
    for diccionario in registro:
        for val in diccionario.values():
            if val == nombre:
                print(diccionario)
    else:
        print('Estudiante no encontrado')
    

def eliminar_estudiante(registro):
    nombre= input('Nombre: ')
    for diccionario in registro:
        for val in diccionario.values():
            if val == nombre:
                registro.remove(diccionario)
    else:
        print('Estudiante no encontrado')
    

while True:
    print('Opciones:')
    print('1. Agregar Estudiante')
    print('2. Mostrar Estudiantes')
    print('3. Buscar Estudiante')
    print('4. Eliminar Estudiante')
    print('5. Salir')
    
    opcion = input('Elija una opcion\n')
    
    if opcion == '1':
        agregar_estudiante(registro1)
    elif opcion == '2':
        mostrar_estudiantes(registro1)
    elif opcion == '3':
        buscar_estudiante(registro1)
    elif opcion == '4':
        eliminar_estudiante(registro1)
    elif opcion == '5':
        break
    else:
        print('Opcion no valida, presione un numero del 1 al 5')

            
    
