#01 Dada una lista de números, crea una nueva lista que contenga el cuadrado de cada número.
'''
numbers = [1, 2, 3, 4, 5]


cuadrado = [number**2 for number in numbers]
print('Cuadrado: ',cuadrado)

cuad = []
for numero in numbers:
    cuad.append(numero**2)
    
print('Cuad: ',cuad)

'''

# 02 Dada una lista de palabras, crea una nueva lista que contenga la longitud de cada palabra.
'''

words = ["python", "is", "fun"]

longitud = [len(word) for word in words]
print(longitud)


long = []
for word in words:
    long.append(len(word))


print(long)

'''


# 03 Dada una lista de números, crea una nueva lista que contenga solo los números pares.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [number for number in numbers if number % 2 == 0]
print(pares)


par = []
for number in numbers:
    if number % 2 == 0:
        par.append(number)
        
print(par)

'''


# 04 Dada una lista de palabras, crea una nueva lista que contenga solo las palabras que tienen más de 3 letras.

'''
words = ["cat", "dog", "elephant", "lion", "bird"]
'''

#List comprehension:
'''
mas_de_3 = [word for word in words if len(word) > 3]

print(mas_de_3)
'''

#For loop:
'''
palabras_largas = [word for word in words if len(word) > 3]
print(palabras_largas)


pal = []

for word in words:
    if len(word) > 3:
        pal.append(word)
        
print(pal)
'''



#05 Dadas dos listas, crea una nueva lista que contenga las parejas de elementos en la misma posición sumados.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

#List comprehension:

suma = [x + y for x , y in zip(list1, list2)]
print(suma)

#For loop:
'''
suma2= []
for x, y  in zip(list1, list2):
    suma2.append(x + y)
    
print(suma2)
   ''' 


#06 Dada una cadena de texto, crea una lista que contenga la longitud de cada palabra, excluyendo los espacios.



#sentence = "Python is an amazing language"

#list comprehension: 
'''
longit = [len(word) for word in sentence.split()]

print(longit)

'''

# For loop:
'''
lista = sentence.split()
long = []

for palabra in lista:
    long.append(len(palabra))
    


x = [len(palabra) for palabra in sentence.split()]


print(lista)
print(long)

'''



# 07 Dada una lista de números, crea una nueva lista que contenga el cuadrado de los números pares y el cubo de los números impares.
'''
numbers = [1, 2, 3, 4, 5, 6]
'''
# List comprehension:
'''
total1 = [num**2 if num % 2 ==0 else num**3 for num in numbers]
print(total1)

'''

#For loop:
'''
final= []
for num in numbers:
    if num %2 == 0:
        final.append(num**2)
    else:
        final.append(num**3)
        
print(final)
   
'''

part = [1, 2 , 3, 4,5,6,7,8,9]
row_square = '|'.join(str(item) for item in part)
print(row_square)


all(self.board[row][col] != num for row in range(9))


# Walrus operator :=
if (next_empty := self.find_empty_cell()) is None: