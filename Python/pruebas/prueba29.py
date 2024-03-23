

#Ordena la lista de menor a mayor usando la función sorted y luego modifica la lista original utilizando el método sort.
# Imprime ambas versiones de la lista.
'''
numbers = [4, 2, 7, 1, 9, 3]

num2 = sorted(numbers)
print(numbers)
numbers.sort()

print(numbers)
print(num2)

'''

# Ordena la lista de palabras por longitud, de la palabra más corta a la más larga, utilizando tanto sorted como el método sort.
# Imprime ambas versiones de la lista.
'''
words = ["apple", "banana", "kiwi", "orange", "strawberry"]

w= sorted(words, key=len)
print(words)
words.sort(key=len)


print(words)
print(w)
'''

# Ordena la lista de tuplas primero por la primera coordenada y luego por la segunda coordenada. Utiliza la función sorted para cada
# clasificación y luego imprime la lista resultante.
 
'''
points = [(1, 2), (3, 1), (0, 4), (5, 2), (2, 2)]

points1= sorted(points)

points2 = sorted(points, key= lambda x: x[1])

print(points1)
print(points2)

'''

# Define una clase llamada Person con atributos name y age. Crea una lista de instancias de esta clase y ordénalas por edad utilizando la 
# función sorted y el método sort. Imprime la lista ordenada.


'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35), Person("David", 28)]


ordenada = sorted(people, key= lambda x: x.age)

print([(a.name, a.age) for a in ordenada])



'''




