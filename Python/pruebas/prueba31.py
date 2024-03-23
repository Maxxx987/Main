

s = ''


porcentajes = {'auto' : 96, 'aserradero' : 45, 'casaremolque': 67}


for i in range(100, -1, -10):
    s1 = f'{i}|'
    s += f'{s1:>4} '
    for key, value in porcentajes.items():
        if value >= i:
            s+= 'o   '
        else:
            s+= '    '

    s+= '\n'
    
s+= '--'* (len(porcentajes) +5) +'\n'



max_len = max(len(key) for key in porcentajes)


for i in range(max_len):
    s+= '     '
    for obj in porcentajes:
        if i <= len(obj) -1:
            s += obj[i] + '   '
        else:
            s += '    '
    s+= '\n'
        

    
print(s)











