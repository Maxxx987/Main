
s = ''
x = {'auto' : 31, 'casa' : 97, 'avion': 74}

for i in range(100, -1, -10):
    m= f'{i}|'
    s+= f'{m:>4}'
    for val in x.values():
        if val >= i:
            s+= ' o  '
        else:
            s+= '    '
        
    s+= '\n'    
    
s+= '-' * (4 + (len(x)* 4)) + '\n' + '    '

longest = max(len(key) for key in x)

for i in range(longest):
    for key in x:
        if i <= len(key)-1:
            s+= f' {key[i]}   ' 
        else:
            s+= '    '
        
    s+= '\n'    
    

print('')
print(s)