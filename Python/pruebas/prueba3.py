
libros= {}


#Título
#Autor
#Año de publicación
#Género
#Número de páginas

def agregar_libro():
    titulo= input('Titulo: ')
    autor= input('Autor: ')
    año= input('Año de publicacion: ')
    genero= input('Genero: ')
    paginas= input('Numero de paginas: ')
    
    libros[titulo]= {'autor': autor, 'año': año, 'genero': genero, 'paginas': paginas}
    
def buscar_libro(titulo):
    print(libros[titulo])
    
def listar_libros():
    print(libros)
    
def actualizar_libro(titulo):
    atributo = input('¿Que atributro desea modificar: ')
    print(f'Valor previo: {libros[titulo][atributo]}')
    valor= input('Ingrese nuevo valor')
    libros[titulo][atributo]= valor
    print(f'Libro actualizado correctamente\n{libros[titulo]}')
    
def eliminar_libro(titulo):
    libros.pop(titulo)
    print('Libro eliminado correctamente')
    
while True:
    print('-----------Menu---------')
    print('1- Agregar Libro')
    print('2- Buscar Libro')
    print('3- Listar Libros')
    print('4- Actualizar Libros')
    print('5- Eliminar Libro')
    print('6- Exit')
    
    
    inp= input('Ingrese numero de opcion: ')
    
    if inp == '1':
        agregar_libro()
    elif inp == '2':
        tit= input('Titulo: ')
        buscar_libro(tit)
    elif inp == '3':
        listar_libros()
    elif inp == '4':
        tit= input('Titulo: ')
        actualizar_libro(tit)
    elif inp == '5':
        tit= input('Titulo: ')
        eliminar_libro(tit)
    elif inp == '6':
        print('Saliendo...\nCompletado')
        break
    else:
        print('Opcion no valida, elija un numero del menú')
    
    