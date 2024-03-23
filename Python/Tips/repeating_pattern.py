pattern = ['A', 'B', 'C']

for i in range(1, 11):
    item = pattern[i % len(pattern)]
    print(f"Item {i}: {item}")