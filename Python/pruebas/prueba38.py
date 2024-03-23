class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        print(f'Hola soy {self.nombre} y tengo {self.edad} años')
            

persona1 = Persona('Alberto', 41)
persona2 = Persona('Mariana', 23)

persona1.presentarse()
persona2.presentarse()