
friends = ['Joseph', 'Jenny', 'Fredd']

#Loop 1:
for friend in friends:
    print(friend)
    
#Loop 2:
for i in range(len(friends)):
    print(friends[i])
    
    
# lista de tuplas a diccionario

lst = [('Jose', 2), ('Juan', 56), ('Alberto', 4)]
dc = {}

for key, val in lst:
    dc[key] = val
    
print(dc)