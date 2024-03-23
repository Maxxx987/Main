class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
        
    def calcular_area(self):
        area = self.base * self.altura
        return area
        
    def calcular_perimetro(self):
        perimetro = (self.base + self.altura) * 2
        return perimetro
    
    
r1 = Rectangulo(10,20)


print(r1.calcular_area())

print(r1.calcular_perimetro())
        