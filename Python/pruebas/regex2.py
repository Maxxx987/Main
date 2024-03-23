
import re
criterio = r'(\w+)\s[a-zA-Z]+y[a-zA-Z]+\s(\w+)'

with open('D:\\Users\\Maxi\\Desktop\\005.txt') as fhand:
    for line in fhand:
        line = line.rstrip()
        line = re.findall(criterio,line )
        if line:
            print(f'{line =}')



'''
criterio = r'\b\S{3}\b'
with open('D:\\Users\\Maxi\\Desktop\\005.txt') as fhand:
    for line in fhand:
        line = line.rstrip()
        line1= re.findall(criterio, line)
        for word in line1:
            x= re.search(criterio, word)
            if x:
                print(word)
        

'''










