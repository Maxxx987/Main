import re

def validar_correo(correo):
    # Expresión regular para validar direcciones de correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Comprobar si la cadena cumple con el patrón
    if re.match(patron, correo):
        print(f'{correo} es una dirección de correo electrónico válida.')
    else:
        print(f'{correo} no es una dirección de correo electrónico válida.')

# Solicitar al usuario ingresar una dirección de correo electrónico
direccion_correo = input('Ingresa una dirección de correo electrónico: ')

# Validar la dirección de correo electrónico ingresada
validar_correo(direccion_correo)
