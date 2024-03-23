class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.materias = []
        
    def agregar_materia(self, materia):
        self.materias.append(materia)
        
    def mostrar_informacion(self):
        print(self.nombre, self.edad, self.materias)
        
    def doblar_edad(self):
        self.edad *= 2
        
        

juan = Estudiante('Juan', 20)
juan.agregar_materia('Matematica')
juan.agregar_materia('Historia')    
maria = Estudiante('Maria', 22)
maria.agregar_materia('Biologia')

juan.mostrar_informacion()

maria.mostrar_informacion()

juan.doblar_edad()


juan.mostrar_informacion()

maria.mostrar_informacion()
