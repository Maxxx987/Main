import re

# re.search() returns True or False

# re.findall() returns a list

#re.match()

# re. sub sustituye una palabra por otra
# new_text = re.sub(pattern, replacement, text)

'''
\w - Carácter de palabra
\d - Dígito
\s - Espacio en blanco
\b: Indica un límite de palabra, asegurando que la fecha esté delimitada por caracteres que no son de palabra (como espacios, comas, etc.).
{n} - Repetición exacta: {n} especifica que el elemento anterior debe repetirse exactamente n veces. Por ejemplo, \d{3} coincide con
exactamente tres dígitos.
| - Barra vertical Alternancia:
La barra vertical | se utiliza para expresar alternativas. En el ejemplo, (patrón1|patrón2|patrón3) significa que el patrón puede coincidir
con patrón1 o patrón2 o patrón3.
. - Cualquier caracter
* - many
+ - uno o mas
? - Non greedy





'''