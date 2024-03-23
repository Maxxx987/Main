class Circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        area = 3.14159 * self.radio **2
        return area
    
    def calcular_perimetro(self):
        perimetro = 2 * 3.14159 * self.radio
        return perimetro


c1 = Circulo(100)



print(c1.radio)

print(c1.calcular_area())

print(c1.calcular_perimetro())