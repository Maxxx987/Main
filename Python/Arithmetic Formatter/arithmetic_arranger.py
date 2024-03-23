def arithmetic_arranger(problems, solve = False):

  first = ''
  second = ''
  lines = ''
  result = ''
  arranged_problems = ''

  if len(problems) > 5:
    return 'Error: Too many problems.'


  for problem in problems:
    f_num = problem.split()[0]
    sign = problem.split()[1]
    s_num = problem.split()[2]



    if sign != '+' and sign != '-':
      return "Error: Operator must be '+' or '-'."

    if f_num.isdigit() == False:
      return 'Error: Numbers must only contain digits.'
    if s_num.isdigit() == False:
      return 'Error: Numbers must only contain digits.'
      


    if len(f_num) >4:
      return 'Error: Numbers cannot be more than four digits.'
    if len(s_num) >4:
      return 'Error: Numbers cannot be more than four digits.'

    width = max(len(f_num), len(s_num)) +2

    
    if sign == '+':
      r = int(f_num) + int(s_num)
    else:
      r = int(f_num) - int(s_num)
      

    
    if problem == problems[-1]:
      first += f_num.rjust(width)
      second += sign + s_num.rjust(width - 1)
      lines += '-' * width
      result += str(r).rjust(width)
      
    else:
      first += f_num.rjust(width) + '    '
      second += sign + s_num.rjust(width - 1) + '    '
      lines += '-' * width + '    '
      result += str(r).rjust(width) + '    '

  

  if solve == True:
    arranged_problems = first + '\n' + second + '\n' + lines +       '\n' + result
  else:
    arranged_problems = first + '\n' + second + '\n' + lines


  return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))