x = ['a' , 'b' , 'c']

for i in range(1,11):
    b = x[i % len(x)-1]
    print(i, b)