with open('4.txt', 'r') as f:
    puzzle = [x.strip().split(',') for x in f.readlines()]

iterations = [[[z for z in range(int(x.split('-')[0]), int(x.split('-')[1])+1)] for x in y] for y in puzzle]

count = 0
for a in iterations:
    if any(numbers in a[0] for numbers in a[1]) or any(numbers in a[1] for numbers in a[0]):
        count += 1
        
print(count)