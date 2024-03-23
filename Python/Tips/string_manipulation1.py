l = ['auto', 'albañil', 'casa', 'cabaña']

# Encuentra la longitud máxima de las palabras en la lista
longitud_maxima = max(len(palabra) for palabra in l)

# Variable para almacenar las letras
resultado = ''

# Itera a través de las letras
for i in range(longitud_maxima):
    for palabra in l:
        # Agrega la letra correspondiente a la variable, o un espacio si no existe
        resultado += palabra[i] if i < len(palabra) else ' '
    # Agrega un salto de línea después de cada fila
    resultado += '\n'

# Imprime el resultado al final
print(resultado)


#lo mismo pero con while:
'''

lista = ['auto', 'albañil', 'casa', 'cabaña']

longitud_maxima = max(len(palabra) for palabra in lista)

string = ''

i = 0

while i < longitud_maxima:
    for palabra in lista:
        if i < len(palabra):
            string += palabra[i]
        else:
            string += ' '
    
    string += '\n'
    
    i += 1
    
    
print(string)
            
'''