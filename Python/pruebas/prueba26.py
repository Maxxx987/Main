

count = 0
x = []
y = ''
for i in range(10):
    print('Count: ', count)
    count += 1
    for b in range(10):
        x.append(i)
        x.append(b)
        continue
        y += str(i)
        y += str(b)

print(x)
print(y)