class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    
    def mostrar_informacion(self):
        print(f'\n{self.nombre} {self.salario} ', end = '')
        

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'{self.departamento}', end = '')
   
    
    
class Asistente(Empleado):
    def __init__(self, nombre, salario, proyecto):
        super().__init__(nombre, salario)
        self.proyecto =proyecto
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'{self.proyecto}', end = '')
    
    
empleado_generico = Empleado("Juan Pérez", 50000)
gerente1 = Gerente("María García", 80000, "Recursos Humanos")
asistente1 = Asistente("Carlos López", 35000, "Desarrollo de Software")

empleado_generico.mostrar_informacion()
gerente1.mostrar_informacion()
asistente1.mostrar_informacion()

