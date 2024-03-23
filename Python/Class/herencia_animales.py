


class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrar_informacion(self):
        print(f'Animal: {self.nombre} Edad: {self.edad}')
        
    
class Mamifero(Animal):
    def __init__(self, nombre, edad, tipo_de_pelo):
        
        #Es necesario poner self aqui?
        super().__init__(nombre, edad)
        self.tipo_de_pelo = tipo_de_pelo
    

    def mostrar_informacion(self):
        
        super().mostrar_informacion()
        print(f'Tipo de pelo: {self.tipo_de_pelo}')
            
        
        
    
class Ave(Animal):
    def __init__(self,  nombre, edad, tipo_plumaje):
        super().__init__(nombre, edad)
        self.tipo_plumaje = tipo_plumaje
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Tipo de plumaje: {self.tipo_plumaje}')
        
        
aguila = Ave('Aguila', 8, 'Marron')
lechuza = Ave('Lechuza', 4, 'Gris')
guepardo = Mamifero('Guepardo', 12, 'Atigrado')

aguila.mostrar_informacion()
print('-' * 20)
lechuza.mostrar_informacion()
print('-' * 20)
guepardo.mostrar_informacion()
print('')