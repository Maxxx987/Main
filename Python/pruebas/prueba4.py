class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrar_informacion(self):
        print('\n-Titulo:', self.titulo, '    -Autor:' , self.autor, '\n')
        

l1 =  Libro("El Principito", "Antoine de Saint-Exupéry")

l2 = Libro("1984", "George Orwell")

l1.mostrar_informacion()

l2.mostrar_informacion()


