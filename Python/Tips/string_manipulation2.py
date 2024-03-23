lista = ['auto', 'albañil', 'casa', 'cabaña']

# Calcular la longitud de la palabra más larga
longitud_maxima = max(len(palabra) for palabra in lista)
string = ''

for index in range(longitud_maxima):
    for i, palab in enumerate(lista):
        if index < len(palab):
            string += palab[index]
        else:
            string += ' '
        
        # Agregar espacio entre las palabras verticales a todas las letras menos la ultima
        if i < len(lista) - 1:
            string += ' '
    
    string += '\n'

print(string)