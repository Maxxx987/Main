class Estudiantes:
    def __init__(self):
        self.registro_estudiantes = []
        
    def agregar_estudiante(self, est= input('Nombre: ') , edad = input('Edad: ')):
        
        estudiante = {'Nombre: ' : est, 'Edad: ' : edad}
        self.registro_estudiantes.append(estudiante)
        
        
    def mostrar_estudiante(self):
        print(self.registro_estudiantes)
        
    def buscar_estudiante(self, busc = input('Nombre: ')):
        for diccionario in self.registro_estudiantes:
            for key in diccionario():
                if key == busc:
                    print(diccionario)
                    break
        print('No se encuentra el estudiante')
        
    def eliminar_estudiante(self, busc = input('Estudiante: ')):
        for diccionario in self.registro_estudiantes:
            for key in diccionario:
                if key == busc:
                    self.registro_estudiantes.remove(diccionario)
                    break
        print('No se encuentra el estudiante')
        
    
                    
curso = Estudiantes()

curso.agregar_estudiante()

curso.mostrar_estudiante
                
        