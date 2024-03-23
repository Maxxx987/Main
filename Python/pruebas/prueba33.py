
'''
import random

gen = ['A', 'T', 'C', 'G']


dna = random.choices(gen, k= 10)

dicc= {index : [value, ('A' if value == 'T' else 'T' if value == 'A' else 'G' if value == 'C' else 'C')] for index, value in enumerate(dna)}

print(dicc)
'''

'''
diccionario = {}
for index, value in enumerate(dna):
    if value == 'A':
        value2 = 'T'
    elif value == 'T':
        value2 = 'A'
    elif value == 'C':
        value2 = 'G'
    else:
        value2 = 'C'
    diccionario[index] = [value, value2] 
    
print(diccionario)
'''







