
import random

bases = ['A', 'T', 'C', 'G']

strand1 = random.choices(bases, k= 10)


dna = {index : [value, ('T' if value == 'A' else 'A' if value == 'T' else 'G' if value == 'C' else 'C')] for (index, value) in enumerate(strand1)}

#[dna[value] = 'T' if value == 'A' else dna[value] = 'A' if value == 'T' else dna[value] = 'G' if value == 'C' else dna[value] = 'C']

print(dna)

'''
print(strand1)

final= []
dna= {}

for index, value in enumerate(strand1):
    if value == 'A':
        value2 = 'T'
    elif value =='T':
        value2 = 'A'
    elif value == 'C':
        value2 = 'G'
    else:
        value2 = 'C'
    
    dna[index] = [value, value2]

print(dna)

'''




















