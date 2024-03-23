class Libro:
    def __init__(self, titulo, autor, año_de_publicacion = None):
        self.titulo = titulo
        self.autor = autor
        self.año_de_publicacion = año_de_publicacion
        self.prestado = False


class Biblioteca:
    def __init__(self):
        
        self.lista = []
        
        
    def agregar_libro(self, libro):
        self.lista.append(libro)
        
        
        
    def prestar_libro(self, titulo):
        busc = self.buscar_libro(titulo)
        
        if busc:
            if busc.prestado == False:
                print(f'Aqui tiene el libro: {busc.titulo}, disfrute la lectura!')
                busc.prestado = True
            else:
                print('Libro no disponible')

            
  
        
        
    def mostrar_libros(self):
        print('\n')
        for libro in self.lista:
            print(f'{libro.titulo} {libro.autor} {libro.año_de_publicacion} {"(No disponible)" if libro.prestado  else "(Disponible)"}')
        print('\n', libro)
        
            
            
    def buscar_libro(self, titu):
        for libro in self.lista:
            if libro.titulo.lower() == titu.lower():
                return libro
            else:
                return None
            
        
        
        
libro1= Libro("Python Crash Course", "Eric Matthes", 2015)
libro2=Libro("Clean Code", "Robert C. Martin", 2008)
libro3=Libro("The Pragmatic Programmer", "Andrew Hunt, David Thomas", 1999)


biblioteca1 = Biblioteca()


biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)
biblioteca1.agregar_libro(libro3)
            
biblioteca1.mostrar_libros()

biblioteca1.prestar_libro("Python Crash Course")

biblioteca1.mostrar_libros()

biblioteca1.buscar_libro("Clean Code")


        