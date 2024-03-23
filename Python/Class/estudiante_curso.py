class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.cursos = []
        
    def isncribirse(self, *cursos):
        curs = []
        for curso in cursos:
            self.cursos.append(curso)
            curso.estudiantes_matriculados.append(self)
            curs.append(curso.nombre_curso)
        print(f'\nEstudiante {self.nombre} se inscribio a {curs}')
            
            
        
    
    def mostrar_cursos(self):
        print(f'\nEl estudiante {self.nombre} esta inscrito a los siguientes cursos:')
        for curso in self.cursos:
            print(f'{curso.nombre_curso}')
            
        
        
        
class Curso:
    def __init__(self, nombre_curso, codigo):
        self.nombre_curso = nombre_curso
        self.codigo = codigo
        self.estudiantes_matriculados = []
        
    
    def añadir_estudiante(self, estudiante):
        self.estudiantes_matriculados.append(estudiante)
        estudiante.cursos.append(self)
    
    def mostrar_estudiantes(self):
        print(f'\nCurso {self.nombre_curso} tiene los siguientes estudiantes:')
        for estudiante in self.estudiantes_matriculados:
            print(f'{estudiante.nombre}{estudiante.edad}')



est1 = Estudiante('Julio Cortazar', 19)
est2 = Estudiante('Maria Rodirguez', 20)
est3 = Estudiante('Alberto Gonzalez', 18)
        
        
curso1 = Curso('Matematica', 'MAT101')
curso2 = Curso('Geografia', 'GEO101')
curso3 = Curso('Historia', 'HIS101')


est1.isncribirse(curso1,curso2,curso3)
est2.isncribirse(curso1,curso3)
est3.isncribirse(curso1,curso2)


est1.mostrar_cursos()
est2.mostrar_cursos()
est3.mostrar_cursos()


curso1.mostrar_estudiantes()
curso2.mostrar_estudiantes()
curso3.mostrar_estudiantes()