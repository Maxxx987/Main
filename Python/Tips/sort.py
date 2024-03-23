

# Dada la siguiente lista de números, ordénalos de menor a mayor utilizando tanto sort como sorted.
'''
numeros = [4, 1, 8, 3, 5, 2]

numeros.sort()

sorted2 = sorted(numeros)

print(numeros)
print(sorted2)

'''
# Ordena alfabéticamente la siguiente lista de palabras utilizando tanto sort como sorted.

'''
palabras = ['manzana', 'banana', 'pera', 'kiwi', 'uva']

sorted3 = sorted(palabras)

palabras.sort()


print(sorted3)
print(palabras)

'''
# Dada la lista de números, ordénala en orden descendente (de mayor a menor) utilizando tanto sort como sorted.
'''

numeros_descendentes = [9, 2, 7, 4, 1, 6]

s1 = sorted(numeros_descendentes, reverse= True)

numeros_descendentes.sort(reverse=True)

print(s1)
print(numeros_descendentes)

'''
# Dada la siguiente lista de tuplas, ordénala por el segundo elemento de cada tupla utilizando tanto sort como sorted.

'''
tuplas = [(3, 6), (1, 8), (2, 4), (5, 7)]

s2 = sorted(tuplas, key= lambda x: x[1])

tuplas.sort(key= lambda x: x[1])

print(s2)
print(tuplas)
'''
# Dada la siguiente lista de cadenas, ordénala por la longitud de cada cadena utilizando tanto sort como sorted.
'''
cadenas = ['python', 'javascript', 'java', 'c', 'ruby']

s3 = sorted(cadenas,key=len)

cadenas.sort(key=len)

print(cadenas)
print(s3)

'''


# Dada la siguiente lista que contiene números, cadenas y booleanos, ordénala de manera que los números vengan primero,
# seguidos por las cadenas y finalmente los booleanos. Utiliza tanto sort como sorted.

'''
mixta = [4, 'apple', True, 2, 'banana', False, 7, 'orange']
'''
#Este metodo no me funciona:
'''
# Con sort (in-place)
mixta = [4, 'apple', True, 2, 'banana', False, 7, 'orange']
mixta.sort(key=lambda x: (isinstance(x, bool), isinstance(x, str), x))
print(mixta)
'''
'''
# Con sorted (crea una nueva lista)
mixta = [4, 'apple', True, 2, 'banana', False, 7, 'orange']
nueva_lista = sorted(mixta, key=lambda x: (isinstance(x, bool), isinstance(x, str), x))
print(nueva_lista)

'''
# Con un for loop:
'''
numeros = []
cadenas = []
booleanos = []

# Clasificar elementos en las listas respectivas
for elemento in mixta:
    if isinstance(elemento, int):
        numeros.append(elemento)
    elif isinstance(elemento, str):
        cadenas.append(elemento)
    elif isinstance(elemento, bool):
        booleanos.append(elemento)

# Combina las listas ordenadas
mixta_ordenada = sorted(numeros) + sorted(cadenas) + sorted(booleanos)

print(mixta_ordenada)

'''

# Ordenar diccionario:
'''
a = 'En un salón hay 1.200 objetos con los que Chuck Norris podría matarte. Incluido el propio salón Chuck Norris murió hace 10 años.
Solo que la muerte no ha tenido el valor de decírseloSi Chuck Norris llega tarde, más le vale al tiempo ir despacio Chuck Norris dona
sangre frecuentemente a la Cruz Roja. Solo que nunca es la suya'

a= a.lower()
a = a.split()


c= {}

for palabra in a:
    c[palabra] = c.get(palabra, 0) +1

ordenada = dict(sorted(c.items(), key=lambda x: x[1], reverse= True))

print(ordenada)
'''

# Ordenar por el primer valor y cuando el primer valor es igual ordenar por el segundo valor en orden descendente
'''
list_tupples = [(1, 9), (1,23),(1, 4),(1, 5),(2, 4),]


ordenada = sorted(list_tupples, key= lambda x: (x[0], -x[1]))

print(ordenada)

'''




