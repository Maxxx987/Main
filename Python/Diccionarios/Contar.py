

hat = ['red','blue','red', 'green', 'green', 'green','red', 'blue', 'green' ]
counts = {}

#Metodo 1

for item in hat:
    if item not in counts:
        counts[item] = 1
    else:
        counts[item] += 1

print(counts)

        
#Metodo 2

for item in hat:
    counts[item] = counts.get(item, 0) +1
    

print(counts)

#Max value: 

val_mas_grande = max(counts.values())


max_value = {}

for key, value in counts.items():
    if value == val_mas_grande:
        max_value[key] = value
        
                 

print(max_value)
