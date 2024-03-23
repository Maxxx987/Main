
#Ejercicio 1:
#Dada la siguiente lista mixta, ordénala de manera que los números pares aparezcan primero, seguidos por los números impares, y finalmente
# las cadenas. Utiliza una clave personalizada.
'''
mixta_ejercicio1 = [2, 'apple', 7, True, 'banana', 4, False, 'orange', 6]
'''
'''
def clave_personalizada(elemento):
    if isinstance(elemento, int):
        return (0, elemento)  # Números pares primero
    elif isinstance(elemento, bool):
        return (1, not elemento)  # Números impares después
    else:
        return (2, elemento)  # Cadenas al final

# Utiliza la función clave_personalizada en la función sorted
resultado_ejercicio1 = sorted(mixta_ejercicio1, key=clave_personalizada)
print(resultado_ejercicio1)
'''

'''
def clave_personalizada(elemento):
    if isinstance(elemento, int):
        if elemento % 2 == 0:
            return (0, elemento)  # Números pares
        else:
            return (1, elemento)  # Números impares
    elif isinstance(elemento, bool):
        return (2, not elemento)  # Booleanos
    else:
        return (3, elemento)  # Cadenas

resultado_ejercicio1 = sorted(mixta_ejercicio1, key=clave_personalizada)
print(resultado_ejercicio1)

'''
'''

def clave_personalizada(elemento):
    if isinstance(elemento, int):
        if elemento % 2 == 0:
            return (0, elemento)  # Números pares
        else:
            return (1, elemento)  # Números impares
    elif isinstance(elemento, bool):
        return (2, elemento)  # Booleanos
    else:
        return (3, elemento)  # Cadenas

resultado_ejercicio1 = sorted(mixta_ejercicio1, key=clave_personalizada)
print(resultado_ejercicio1)

'''



# Ordena la siguiente lista de tuplas por el tercer elemento de cada tupla de manera descendente.
'''
tuplas_ejercicio2 = [(1, 5, 3), (2, 8, 1), (4, 6, 9), (7, 2, 5)]

ordenadas = sorted(tuplas_ejercicio2, key= lambda x: x[2], reverse= True)

print(ordenadas)
'''

# Ordena la siguiente lista de diccionarios por el valor asociado con la clave 'edad'.


'''
personas = [{'nombre': 'Ana', 'edad': 25}, {'nombre': 'Juan', 'edad': 20}, {'nombre': 'Eva', 'edad': 30}]

resultado = sorted(personas, key= lambda x: x['edad'])

print(resultado)
'''


# Ejercicio 4:
# Dada la siguiente lista de fechas en formato 'dd-mm-yyyy', ordénala de la más antigua a la más reciente.

fechas = ['15-02-2020', '03-12-2021', '22-08-2019', '10-06-2022']


'''
def convertir_fecha(fecha):
    dia, mes, ano = fecha.split('-')
    return ano, mes, dia
    



ordenadas = sorted(fechas, key= convertir_fecha)

print(ordenadas)

'''

# Ejercicio 5:
# Ordena la siguiente lista de palabras por la cantidad de vocales de cada palabra.
'''
palabras = ['python', 'javascript', 'java', 'c', 'ruby', 'eeeeee', 'o']


ordenada = sorted(palabras, key= lambda x: sum(1 for letra in x if letra in 'aeiou'))
print(ordenada)
'''
'''
def vocales(palabra):
    num = 0
    vocal = 'aeiou'
    for letra in palabra:
        if letra in vocal:
            num += 1
    return num


ordenada = sorted(palabras, key= vocales)
print(ordenada)

'''

# Ejercicio 6:
# Dada la siguiente lista de nombres, ordénala alfabéticamente ignorando mayúsculas y minúsculas.
'''
nombres = ['Carlos', 'ana', 'Pedro', 'maria', 'Juan']

ord = sorted(nombres, key= lambda x: x.lower())

print(ord)
'''



# Ordenar por el primer valor y cuando el primer valor es igual ordenar por el segundo valor en orden descendente
'''
list_tupples = [(1, 9), (1,23),(1, 4),(1, 5),(2, 4),]


ordenada = sorted(list_tupples, key= lambda x: (x[0], -x[1]))

print(ordenada)

'''


