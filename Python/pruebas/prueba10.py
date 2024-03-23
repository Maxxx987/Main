l = ['auto', 'albañil']

# Encuentra la longitud máxima de las palabras en la lista
longitud_maxima = max(len(palabra) for palabra in l)

# Itera a través de las letras
for i in range(longitud_maxima):
    temp_string = ''
    for palabra in l:
        temp_string += palabra[i]
        # Imprime la letra correspondiente si existe, de lo contrario imprime un espacio
        print(palabra[i] if i < len(palabra) else ' ', end='')
    # Salto de línea después de imprimir las letras de cada palabra
    print()