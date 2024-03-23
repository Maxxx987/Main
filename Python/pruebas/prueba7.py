class Libro:
    def __init__(self, titulo, autor, disponible = True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible
        
    def prestar_libro(self):
        if self.disponible:
            self.disponible = False
            print('Aqui tienes, que disfrutes de la lectura\n')
        else:
            print('El libro no se encuentra disponible\n')
            
    def devolver_libro(self):
        if self.disponible == False:
            self.disponible = True
            print('Muchas gracias por devolverlo!\n')
        else:
            print('Ese libro ya ha sido devuelto, ¿estas seguro que lo retiraste de aquí?\n')
    
    def mostrar_informacion(self):
        if self.disponible:
            disp = 'Estado: Disponible'
        else:
            disp = 'Estado: No disponible'
        
        print(f'Titulo: {self.titulo} Autor:  {self.autor} {disp}')
        
lib1 = Libro("El Hobbit" , "J.R.R. Tolkien")

lib1.mostrar_informacion()
lib1.prestar_libro()
lib1.mostrar_informacion()
lib1.devolver_libro()
lib1.mostrar_informacion()

