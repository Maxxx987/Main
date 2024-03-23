
import re


patron = r'^[0-9]+$'

s = '87 4'


if re.search(patron, s):
    print('Patron valido: ',s)
else: print('Patron no valido: ',s)



