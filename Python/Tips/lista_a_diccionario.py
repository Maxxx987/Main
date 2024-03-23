

def lista_a_diccionario(lista):
    diccionario = {}

    for elemento in lista:
        diccionario[elemento] = diccionario.get(elemento, 0) + 1

    return diccionario

# Ejemplo de uso:
list1 = ["red", "red", "green", "blue", "blue"]
dic1 = lista_a_diccionario(list1)
print(dic1)