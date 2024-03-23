


ventas = { 'venta1' : {'fecha' : '28/12/2023' ,'productos':{'yerba': '2', 'azucar': '4'}, 'total' : 5000.0},
          'venta2' : {'fecha' : '28/12/2023' ,'productos':{'mantecol': '7', 'pollo': '4'}, 'total' : 5000.0}}


def registrar_venta():
    # Implementar la función para registrar una nueva venta en el diccionario
    fecha = input('Fecha: ')
    compra = {}
    num = len(ventas)+1
    
    
    
    
    while True:
        productos = {}
        while True:
            producto = input ('Producto: ("fin" para salir)')
            if producto.lower() == 'fin':
                break
            cantidad = input(f'Producto: {producto} Cantidad: ')
            productos[producto] = cantidad
        total = float(input('Total: '))
        compra = {'fecha': fecha,'productos': productos,'total' : total}
        break
    
    ventas[f'venta{num}'] = compra
    

def buscar_venta(fecha):
    # Implementar la función para buscar una venta por su fecha
    for venta in ventas:
        if fecha in ventas[venta].values():
            return ventas[venta]
    print('No se encontraron ventas')    
    return None

def listar_ventas():
    # Implementar la función para listar todas las ventas
    print(len(ventas))
    for k, v in ventas.items():
        print(k, v)
        print()
        
    
    

def actualizar_venta(fecha):
    # Implementar la función para actualizar la información de una venta
    print(buscar_venta(fecha))
    modif = input('Elija la venta que quiere modificar')
    
    if modif:
        compra = {}
        while True:
            producto = input ('Producto: ("fin" para salir)')
            if producto.lower() == 'fin':
                break
            cantidad = input(f'Producto: {producto} Cantidad: ')
            total = float(input('Total: '))
            compra[producto] = {'fecha': fecha, 'cantidad' : cantidad, 'total' : total}
        ventas[modif]= compra

def eliminar_venta(fecha):
    # Implementar la función para eliminar una venta del diccionario
    print(buscar_venta(fecha))
    elim = input('Elija la venta que quiere eliminar')
    ventas[elim] = 'Venta eliminada'
    print('Venta eliminada correctamente')
    

# Aquí puedes implementar un menú interactivo para que el usuario realice operaciones



while True:
    print('----------Menu de ventas-----------')
    print('01- Registrar venta')
    print('02- Buscar venta')
    print('03- Listar ventas')
    print('04- Actualizar ventas')
    print('05- Eliminar ventas')
    print('06- Salir')

    a = input('Elija una opcion:\n')
    
    if a == '1':
        registrar_venta()
    elif a == '2':
        fecha = input('Fecha (DD/MM/AAAA): ')
        print(buscar_venta(fecha))
    elif a == '3':
        listar_ventas()
    elif a == '4':
        fecha = input('Fecha de la venta: ')
        actualizar_venta(fecha)
    elif a == '5':
        fecha = input('Fecha de la venta a eliminar: ')
        eliminar_venta(fecha)
    elif a == '6':
        break
    else:
        print('Opcion no valida')
        
        
    
    


