from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_area(self):
        pass

    def mostrar_informacion(self):
        print(f"Figura: {self.nombre}")
        print(f"Área: {self.calcular_area()}")

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Lado: {self.lado}")

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Radio: {self.radio}")

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return 0.5 * self.base * self.altura

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Base: {self.base}")
        print(f"Altura: {self.altura}")

# Crear instancias y mostrar información
cuadrado = Cuadrado(4)
circulo = Circulo(3)
triangulo = Triangulo(5, 6)

cuadrado.mostrar_informacion()
print("-" * 20)
circulo.mostrar_informacion()
print("-" * 20)
triangulo.mostrar_informacion()