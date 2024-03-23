import random

hat = ['red','blue','red', 'green', 'green', 'green','red', 'blue' ]


a = random.sample(hat, 3)

b = {'green': 3 ,'blue': 2, 'red':3}

iterations = 100

for color in a:
    if color in b:
        b[color] -= 1

success = 0
        
for i in range(iterations):
    for key, value in b.items():
        if value < 1:
            success += 1
            break


        
    
    
    
print(a)
print(b)
print(success)