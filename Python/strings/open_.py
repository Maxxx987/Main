
import re

#fhand = neumonic for "file handle"
fhand = open('frases celebres.txt')


text = ''

for line in fhand:
    text += line

print(text)
'''
for line in fhand:
    line = line.rstrip()
    if 'duerme' in line:
        print(line)

'''


'''

for line in fhand:
    line = line.rstrip()
    if line.startswith('Chuck Norris no'):
        print(line)
  '''      
        
        
        
x = re.findall('[0-9]+', text)

print(x)

        
        
        
        
        
        