
import re

def arithmetic_arranger(problems, solve= False):
  first_line = ''
  operation = ''
  second_line = ''
  arranged = ''
  lineas = ''
  criterio = r'^[0-9]+$'
  
  if len(problems) >5:
    return 'Error: Too many problems.'
  
  
    
  
  for problem in problems:
    prob_list = problem.split()
    if prob_list[1] not in '+-':
      return 'Error: Operator must be '+' or '-'.'
    if re.search(criterio, prob_list[0]) and re.search(criterio, prob_list[2]):
    #if prob_list[0].isdigit() and prob_list[2].isdigit():
      pass
    else:
      return 'Error: Numbers must only contain digits.'
      


    mx = max(len(item) for item in prob_list) +2
    
    if solve:
      if prob_list[1] == '+':
        resultado = int(prob_list[0]) + int(prob_list[2])
      else:
        resultado = int(prob_list[0]) - int(prob_list[2])
        
      operation += f'{resultado:>{mx}}    '
        
        
    
    
    a= f'{prob_list[0]:>{mx}}    '
    first_line+= a
    
    b= f'{prob_list[1]} {prob_list[2]:>{mx-2}}    '
    second_line+= b
    lineas+= '-'* mx + '    '
    
    
    
    
    
  if solve:
    arranged = first_line + '\n' + second_line + '\n' + lineas + '\n' + operation
  else:
    arranged = first_line + '\n' + second_line + '\n' + lineas
  
  return arranged
  
print(arithmetic_arranger(["34 + 8", "1 - 287", "9999 + 9999", "523 - 49", "523 - 49"], True))


  