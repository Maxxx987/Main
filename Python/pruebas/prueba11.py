lista = ['auto', 'albañil', 'casa', 'cabaña']

longitud_maxima = max(len(palabra) for palabra in lista)

#proximamente encontrar la palabra mas larga e imprimirla
palabra_mas_larga = ''
for palabra in lista:
    if len(palabra) == longitud_maxima:
        palabra_mas_larga = palabra
print(palabra_mas_larga)
        


string = ''

for index in range(longitud_maxima):
    for palabra in lista:
        if index < len(palabra):
            string += palabra[index]
        else:
            string += ' '
    string += '\n'
print(string)
        
        
        