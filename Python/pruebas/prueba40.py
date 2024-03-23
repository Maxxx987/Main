class Libro:
    def __init__(self, titulo, autor, paginas, clave, disponible = True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.clave= clave
        self.disponible = disponible
        

    def detalles(self):
        
        clave = self.clave.title()
        print()
        print(f'{clave}:')
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Paginas: {self.paginas}')
        print()
    
    
libro1 = Libro('Aaaa', 'Maradona', 1134, 'libro1')
libro2 = Libro('gggggg', 'Sandro', 184, 'libro2')



class Biblioteca:
    def __init__(self):
        self.libros = []


        
        
    def añadir(self, libro):
        self.libros.append(libro)

        
        
    def mostrar(self):
        for libro in self.libros:
            if libro.disponible:
                libro.detalles()
                
    def prestar(self, libro):
        if libro.disponible:
            libro.disponible = False
            print(f'Aqui tiene el libro {libro.titulo}, que disfrute de la lectura')
        else:
            print('El libro no esta disponible')
            
    def devolver(self, libro):
        if libro.disponible == False:
            libro.disponible = True
            print('Libro devuelto, muchas gracias!')
        else: print('Debe haber un error, ese libro ya fue devuelto')
            
        
bib1 = Biblioteca()
bib1.añadir(libro1)
bib1.añadir(libro2)


def ag(nom):
    titulo = input('Titulo: ') 
    autor = input('Autor:')
    paginas = input('Paginas: ')
    lib = Libro(titulo, autor, paginas, nom)
    bib1.añadir(lib)
    print(f'Libro "{nom}" agregado correctamente')
    



while True:
    print('---------Menu Biblioteca--------')
    print('01- Agregar libro')
    print('02- Mostrar libros')
    print('03- Prestar libro')
    print('04- Devolver libro')
    print('05- Salir')
    
    x = input('Elija una opcion\n')
    
    if x == '1':
        nom = f'libro{len(bib1.libros) +1}'
        ag(nom)
    elif x == '2':
        bib1.mostrar()
    elif x == '3':
        libro = input('Libro: ')
        bib1.prestar(libro)
    elif x == '4':
        libro = input('Libro: ')
        bib1.devolver(libro)
    elif x == '5':
        break
    else: print('Opcion no valida, elija otro numero')
        
        
        








