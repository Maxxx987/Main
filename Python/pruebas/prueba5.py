class Calculadora:
    def __init__(self):
        self.resultado = 0
        
        pass
    
    def suma(self, a , b):
        self.resultado = a + b
        print(self.resultado)
       
        
    def resta(self, a , b):
        self.resultado = a - b
        print(self.resultado)
        
    def multiplica(self, a , b):
        self.resultado = a * b
        print(self.resultado)
        
    def divide(self, a , b):
        self.resultado = a / b
        print(self.resultado)
        
    
calcu = Calculadora()

calcu.suma(100, 80)

calcu.resta(879, 78)

calcu.multiplica(15,100)

calcu.divide(80,8)

