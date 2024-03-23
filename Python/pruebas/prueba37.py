


# Biblioteca
biblioteca = {
    'libro1': {
        'titulo': 'El señor de los anillos',
        'autor': 'J.R.R. Tolkien',
        'ano_publicacion': 1954,
        'prestamo': {
            'prestamista': 'Juan Perez',
            'fecha_prestamo': '2023-01-10'
        }
    },
    'libro2': {
        'titulo': 'Cien años de soledad',
        'autor': 'Gabriel García Márquez',
        'ano_publicacion': 1967,
        'prestamo': {
            'prestamista': 'Maria Rodriguez',
            'fecha_prestamo': '2023-02-15'
        }
    },
    # Puedes agregar más libros si lo deseas
}




def agregar_libro():
    
    num = len(biblioteca)+1
    lib = f'libro{num}'
    
    while True:
        titulo = input('Titulo: ')
        autor = input('Autor: ')
        año = input('Año de publicacion: ')
        biblioteca[lib] = {'titulo': titulo, 'autor': autor, 'ano_publicacion': int(año)}
        break
    


# Mostrar información de la biblioteca
def listar_libros():
    for clave, libro in biblioteca.items():
        print(f'Libro: {clave}')
        print(f'Título: {libro["titulo"]}')
        print(f'Autor: {libro["autor"]}')
        print(f'Año de publicación: {libro["ano_publicacion"]}')
        
        if 'prestamo' in libro:
            print(f'Prestamo: {libro["prestamo"]["prestamista"]} el {libro["prestamo"]["fecha_prestamo"]}')
        else:
            print('No está prestado.')
        print('-' * 30)
    
    
    
def prestar_libro():
    for libro in biblioteca:
        print(f'{libro}: {biblioteca[libro]["titulo"]}')
    lib = input('¿Que libro desea prestar?\n')
    for k, v in biblioteca.items():
        for a, b in v.items():
            if lib in b:
                print(v)
                if 'prestamo' in v:
                    print('El libro ya fue prestado')
                else: 
                    prestamista = input('Prestamista: ')
                    fecha = input('Fecha (YYYY/MM/DD): ')
                    biblioteca[libro]['prestamo'] = {'prestamista': prestamista, 'fecha_prestamo': fecha}
    
    
def devolver_libro():
    titulo = input('Titulo: ')
    for k, v in biblioteca.items():
        if titulo in biblioteca[k].values():
            if 'prestamo' in biblioteca[k]:
                biblioteca[k].pop('prestamo')
                print(biblioteca[k])

while True:
    print('--------Menu Biblioteca---------')
    print('1- Agregar libro')
    print('2- Listar libros')
    print('3- Prestar libros')
    print('4- Devolver libros')
    print('5- Salir')

    a = input('Elija una opcion:\n')
    
    if a == '1':
        agregar_libro()
    elif a == '2':
        listar_libros()
    elif a == '3':
        prestar_libro()
    elif a == '4':
        devolver_libro()
    elif a == '5':
        break
    else: print('Opcion no valida, elija un numero')




