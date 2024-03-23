
#Convertir keys en una lista

dicc1 = {'Jose': 2, 'Juan': 56, 'Alberto': 4}
'''
a = list(dicc1)
print('Keys: ',a)
'''
#Convertir values en una lista
'''
b = list(dicc1.values())
print('Values: ', b)
'''
#Convertir key, values en una lista de tuplas
'''
c = list(dicc1.items())
print('Key, Values: ', c)

'''

'''
lis = sorted(dicc1.items(), key= lambda x: x[1])
print(lis)
'''


'''
lst = []
for k, v in dicc1.items():
    lst.append((v, k))

lst = sorted(lst)
print(lst)    

d = {}
for val, key in lst:
    d[key] = val
    
print(d)
'''
    






