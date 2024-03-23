successful = 0
count = 0
expected_balls = {'blue': 2, 'green': 3, 'white': 1}
dic_balls = {'blue': 6, 'green': 2, 'white': 1, 'orange' : 2}

    
    
for key, val in dic_balls.items():
    #expected2 = expected_balls
    print(expected_balls)
    k = expected_balls.get(key, 0)
    if val >= k:
        count += 1
    
    
if count == len(dic_balls):
    successful += 1
    
    
print(successful)