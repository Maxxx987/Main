

libros= {}

'''
Título
Autor
Año de publicación
'''

def agregar_libro():
    titulo= input('Titulo: ')
    autor= input('Autor: ')
    año= input('Año de publicacion: ')
    libros[titulo]= {'Autor': autor, 'Año': año}
    print(f'Libro {titulo} agregado exitosamente')
    
    

def mostrar_libros():
    text = '\nLIBROS:'
    for k, v in libros.items():
        text += f'\nTitulo: {k}  '
        for a, b in v.items():
            text+= f'{a}: {b}  '
    print(text)
    print()
            
        
        
        
        
    
while True:
    print('-------Menu--------')
    print('1- Agregar Libro')
    print('2- Mostrar Libros')
    print('3- Salir')
    
    inp= input('Ingrese un numero de opcion:\n')
    
    if inp == '1':
        agregar_libro()
    elif inp == '2':
        mostrar_libros()
    elif inp == '3':
        break
    else:
        print('Opcion no valida, elija uno de los numeros del menú\n')