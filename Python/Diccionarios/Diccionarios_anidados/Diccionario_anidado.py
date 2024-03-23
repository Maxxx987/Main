


libros = {}

def agregar_libro():
    # Implementar la función para agregar un nuevo libro al diccionario
    '''
Título
Autor
Año de publicación
Género
Número de páginas
'''
    titulo = input('Titulo: ')
    autor = input('Autor: ')
    año = input('Año de publicación: ')
    genero = input('Género: ')
    paginas = input('Número de páginas: ')
    
    libros[titulo] = {'autor' : autor, 'año' : año, 'genero' : genero, 'paginas': paginas}
    print(f'Libro {titulo} agregado exitosamente\n')



def buscar_libro(titulo):
    # Implementar la función para buscar un libro por su título
    if titulo in libros:
        print(libros[titulo])

def listar_libros():
    # Implementar la función para listar todos los libros
    for key in libros.keys():
        print(key)
    print()

def actualizar_libro(titulo):
    # Implementar la función para actualizar la información de un libro
    atributo = input('Que atributo desea modificar? ')
    print(f'{atributo}: {libros[titulo][atributo]}')
    valor = input('Nuevo valor: ')
    libros[titulo][atributo] = valor
    
    print(f'Libro actualizado correctamente: {libros[titulo]}')

def eliminar_libro(titulo):
    # Implementar la función para eliminar un libro del diccionario
    libros.pop(titulo)
    print('Libro eliminado correctamente')
    
    

# Aquí puedes implementar un menú interactivo para que el usuario realice operaciones


while True:
    print()
    print(f'--------------Bienvenido a la Biblioteca:-------------')
    print('Que desea hacer?')
    print('1- Agregar Libro')
    print('2- Buscar Libro')
    print('3- Listar Libros')
    print('4- Actualizar Libro')
    print('5- Eliminar Libro')
    print('6- Salir\n')
 
    inp = input()
    
    
    if inp == '1':
        agregar_libro()
    elif inp == '2':
        lib = input('Titulo: ')
        buscar_libro(lib)
    elif inp == '3':
        listar_libros()
    elif inp == '4':
        tit = input('Título: ')
        actualizar_libro(tit)
    elif inp == '5':
        tit = input('Titulo: ')
        eliminar_libro(tit)
    elif inp == '6':
        break
    else:
        print('No es un numero valido, por favor elija una opcion')
    
    














