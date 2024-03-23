
#convertir numeros decimales a numeros de base 27

'''
def decimal_to_base27(decimal_number):
    if decimal_number < 0:
        raise ValueError("El número decimal debe ser no negativo.")

    if decimal_number == 0:
        return '0'

    base27_digits = []
    while decimal_number:
        decimal_number, remainder = divmod(decimal_number, 27)
        # Convertir el residuo a la letra correspondiente en el alfabeto, A=1, B=2, ..., Z=26
        digit = chr(ord('A') + remainder - 1) if remainder > 0 else 'Z'
        base27_digits.append(digit)

    # Los dígitos se agregaron en orden inverso, así que hay que revertir la lista
    base27_digits.reverse()

    return ''.join(base27_digits)

# Ejemplo de uso
decimal_number = 12345
base27_number = decimal_to_base27(decimal_number)
print(f"Decimal: {decimal_number}, Base 27: {base27_number}")




'''
'''
a, b, c = '1 2 3'.split()

print(a)
print(b)
print(c)


'''

my_dict = {
    "Spider": "photographer", 
    "Bat": "philanthropist", 
    "Wonder Wo": "nurse"
}

my_dict = {(key+ 'man' if key != 'Spider' else 'Superman'): (value if key != 'Spider' else 'journalist') for key, value in my_dict.items()}

print(my_dict)










