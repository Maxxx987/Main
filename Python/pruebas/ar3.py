def arithmetic_arranger(problems, solve=False):
  first_line = ''
  operation = ''
  second_line = ''
  arranged = ''
  lineas = ''

  if len(problems) > 5:
    return 'Error: Too many problems.'

  count = 0
  for problem in problems:
    count += 1
    prob_list = problem.split()
    if prob_list[1] not in '+-':
      return "Error: Operator must be '+' or '-'."
    if prob_list[0].isdigit() and prob_list[2].isdigit():
      pass
    else:
      return 'Error: Numbers must only contain digits.'

    if len(prob_list[0]) >4 or len(prob_list[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    

    mx = max(len(item) for item in prob_list) + 2

    if solve:
      if prob_list[1] == '+':
        resultado = int(prob_list[0]) + int(prob_list[2])
      else:
        resultado = int(prob_list[0]) - int(prob_list[2])

      operation += f'{resultado:>{mx}}'

    a = f'{prob_list[0]:>{mx}}'
    b = f'{prob_list[1]} {prob_list[2]:>{mx-2}}'
    lineas += '-' * mx


    if count < len(problems):
        a += '    '
        b += '    '
        lineas += '    '
        operation += '    '
        
        
    first_line += a
    second_line += b
    
    
  if solve:
    arranged = first_line + '\n' + second_line + '\n' + lineas + '\n' + operation
  else:
    arranged = first_line + '\n' + second_line + '\n' + lineas

  return arranged


