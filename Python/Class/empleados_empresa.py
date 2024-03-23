class Empleado:
    def __init__(self, nombre, apellido, salario, puesto):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.puesto = puesto
        
    
class Empresa:
    def __init__(self):
        self.lista = []
        

    def agregar_empleado(self, empleado):
        self.lista.append(empleado)
        
    
    def mostrar_empleados(self):
        print('\n')
        for empleado in self.lista:
            print(f'Empleado: {empleado.nombre} {empleado.apellido}. Salario: {empleado.salario}$. Puesto: {empleado.puesto}')
    
    
    def buscar(self, nomb):
        for empleado in self.lista:
            if empleado.nombre == nomb:
                return empleado
        return None
    
    def salario_total(self):
        total = 0
        for empleado in self.lista:
            total+= empleado.salario
        print(f'\nEl salario total es: {total}$')
        
    def aumento(self, empleado, nuevo_sal):
        em = self.buscar(empleado)
        if em:
            em.salario = nuevo_sal
            print(f'\nEl nuevo salario de {em.nombre} es {nuevo_sal}$')
        else:
            print(f'\nEmpleado {empleado} no encontrado')



            
empl1 = Empleado('Julio', 'Rodriguez',500,'Supervisor')
empl2 = Empleado('Alfredo', 'Sanchez',800,'Jefe de planta')
empl3 = Empleado('Maria', 'Casenave',300,'Secretaria')

empre1 = Empresa()

empre1.agregar_empleado(empl1)
empre1.agregar_empleado(empl2)
empre1.agregar_empleado(empl3)

empre1.mostrar_empleados()

empre1.salario_total()

empre1.aumento('Maria', 900)
empre1.aumento('Julio', 1500)

empre1.mostrar_empleados()
empre1.salario_total()
        
        