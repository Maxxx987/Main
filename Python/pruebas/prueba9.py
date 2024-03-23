from abc import ABC, abstractmethod
import math

class Figura_geometrica(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
     
     
    @abstractmethod    
    def calcular_area(self):
        pass
    
    
    def mostrar_informacion(self):
        print(f'Figura: { self.nombre}. Area: {self.calcular_area()}. ', end='')
        
class Cuadrado(Figura_geometrica):
    def __init__(self, lado):
        super().__init__('Cuadrado')
        self.lado = lado
        
    
    def calcular_area(self):
        return self.lado ** 2
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Lado: {self.lado}.')
        
        
class Circulo(Figura_geometrica):
    def __init__(self, radio):
        super().__init__('Circulo')
        self.radio = radio
        
    def calcular_area(self):
        return f'{math.pi * self.radio **2:.2f}'
    

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Radio: {self.radio}.')
        

class Triangulo(Figura_geometrica):
    def __init__(self, base, altura):
        super().__init__('Triangulo')
        self.base = base
        self.altura = altura
        
        
    def calcular_area(self):
        return int(self.base * self.altura /2)
    
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Base: {self.base}. Altura: {self.altura}.')
        
    
cuadrado = Cuadrado(4)
circulo = Circulo(7)
triangulo = Triangulo(3 , 8)

print('')
cuadrado.mostrar_informacion()
print('')
circulo.mostrar_informacion()
print('')
triangulo.mostrar_informacion()
print('')
    

        
        
        