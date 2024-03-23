class Libro:
    def __init__(self, titulo, autor, año = None):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.prestado = False
        
class Biblioteca:
    def __init__(self):
        self.lista = []
        

    
    def agregar_libro(self, libro):
        self.lista.append(libro)
        
        
        
    def mostrar_libros(self):
        print('\n')
        for libro in self.lista:
            print(f'{libro.titulo} {libro.autor} {libro.año} {"(No disponible)" if libro.prestado else "(Disponible)"}')
            
    
    
    def buscar(self, tit):
        for libro in self.lista:
            if libro.titulo == tit:
                return libro

        return None
            
    
    def prestar(self, titu):
        busc= self.buscar(titu)
        if busc:
            if busc.prestado == False:
                print(f'\nAqui tienes el libro: {busc.titulo}, que disfrutes de la lectura!')
                busc.prestado = True
            else:
                print(f'\nEl libro {titu} fue prestado, vuelva mañana')
        else:
            print(f'\nLo siento no tenemos el libro {titu}')
     
            
    def devolver(self, t):
        dev = self.buscar(t)
        if dev:  
            dev.prestado = False
            print(f'Gracias por devolver el libro: {t}')
        
        
                
            
lib1 = Libro("Python Crash Course", "Eric Matthes", 2015)
lib2 = Libro("Clean Code", "Robert C. Martin", 2008)
lib3 = Libro("The Pragmatic Programmer", "Andrew Hunt, David Thomas", 1999)

bilblio1 = Biblioteca()

bilblio1.agregar_libro(lib1)
bilblio1.agregar_libro(lib2)
bilblio1.agregar_libro(lib3)

bilblio1.mostrar_libros()

bilblio1.prestar("Clean Code")


bilblio1.prestar("1984")


bilblio1.prestar("Clean Code")


bilblio1.mostrar_libros()

bilblio1.devolver("Clean Code")

bilblio1.mostrar_libros()

        
        

        