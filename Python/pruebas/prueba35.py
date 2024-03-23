

# Define un diccionario anidado con información de estudiantes y sus calificaciones
estudiantes = {
    'estudiante1': {
        'nombre': 'Juan',
        'calificaciones': {
            'matematicas': 90,
            'historia': 80,
            'ciencias': 95
        }
    },
    'estudiante2': {
        'nombre': 'Maria',
        'calificaciones': {
            'matematicas': 75,
            'historia': 92,
            'ciencias': 88
        }
    },
    'estudiante3': {
        'nombre': 'Carlos',
        'calificaciones': {
            'matematicas': 85,
            'historia': 78,
            'ciencias': 90
        }
    }
}



# Completa la siguiente función para obtener la lista de nombres de todos los estudiantes
def obtener_nombres(estudiantes):
    nombres = []
    for key in estudiantes:
        nombres.append(estudiantes[key]['nombre'])
    return nombres
   


# Completa la siguiente función para obtener la calificación de un estudiante en una materia específica
def obtener_calificacion(estudiantes, nombre_estudiante, materia):
    for estudiante in estudiantes:
        if estudiantes[estudiante]['nombre']== nombre_estudiante:
            return estudiantes[estudiante]['calificaciones'][materia]




# Completa la siguiente función para agregar un nuevo estudiante al diccionario
def agregar_estudiante(estudiantes, nombre, calificaciones):
    estudiantes[nombre] = calificaciones
    nomb = estudiantes[nombre]['nombre']
    print(f'Se agrego a {nomb} como {nombre}')

# Prueba las funciones
nombres = obtener_nombres(estudiantes)
print("Nombres de estudiantes:", nombres)

calificacion_maria_ciencias = obtener_calificacion(estudiantes, 'Maria', 'ciencias')
print("Calificación de Maria en Ciencias:", calificacion_maria_ciencias)

nuevo_estudiante = {
    'nombre': 'Ana',
    'calificaciones': {
        'matematicas': 92,
        'historia': 88,
        'ciencias': 95
    }
}
agregar_estudiante(estudiantes, 'estudiante4', nuevo_estudiante)

print("Diccionario actualizado con nuevo estudiante:")
print(estudiantes)
