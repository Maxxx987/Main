
hat = ['red','red','blue','red', 'green', 'green', 'green','red', 'blue', 'green' ]

dicc = {}

#Metodo 1
for i in hat:
    dicc[i] = dicc.get(i, 0) +1
    
print(dicc)

#Metodo 2
for i in hat:
    if i not in dicc:
        dicc[i] = 1
    else:
        dicc[i] += 1
        

print(dicc)

max_val = max(dicc.values())

max_item = {}

for k, v in dicc.items():
    if v == max_val:
        max_item[k] = v
        
print(max_item)