import re

file = open('texto.txt')

string = file.read()



file = open('texto.txt')

fecha = r'\d{4}-\d{2}-\d{2}'
total_fechas= []
count = 0
for line in file:
    count = count +1
    fechas= re.findall(fecha, line)
    total_fechas.append(fechas)
print(f'{count = }')
print(total_fechas)



file.close()


with open('texto.txt') as fhand:
    for line in fhand:
        line = line.rstrip()
        print(line)


print(f'String: {string}')
print('Fin')