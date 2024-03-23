
#Crea una lambda que tome un número como argumento y devuelva el doble de ese número.

'''
doble = lambda x: x * 2

print(doble(8))
'''
# Crea una lambda que tome dos números como argumentos y devuelva su suma.

'''
suma = lambda x, y: x + y
print(suma(8,9))
'''
#Crea una lambda que tome un número como argumento y devuelva True si es par y False si es impar.
'''
par = lambda x: x % 2 == 0

print(par(6))
'''

#Crea una lambda que tome una cadena como argumento y devuelva la cadena en mayúsculas.

'''
mayus = lambda x: x.upper()

print(mayus('assaf'))
'''

#Crea una lambda que tome un número como argumento y devuelva su cuadrado.


'''
cuad = lambda x: x **2
print(cuad(4))
'''

#Crea una lista de tuplas y úsala con sorted y una lambda para ordenar la lista por el segundo elemento de cada tupla.

'''
lista_tuplas = [(1, 5), (3, 2), (2, 8), (4, 1)]

lista_ordenada = sorted(lista_tuplas, key=lambda x: x[1])

print(lista_ordenada)
'''


