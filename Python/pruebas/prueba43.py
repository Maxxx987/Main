class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print('\nHola, ¿como estas? mi nombre es', self.nombre ,'y tengo', self.edad ,'años.\n')
        

Juan = Persona('Juan', 25)

Maria = Persona('Maria', 30)



Juan.saludar()

Maria.saludar()


