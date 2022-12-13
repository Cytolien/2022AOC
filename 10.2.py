with open('10.txt', 'r') as f:
    puzzle = [x.strip().split() for x in f.readlines()]

cycle = 0
X = 1

for a in range(len(puzzle)):
    if len(puzzle[a]) == 1:
        cycle += 1
        puzzle[a].extend([0, cycle, X])
    else:
        cycle += 2
        X += int(puzzle[a][1])
        puzzle[a].extend([cycle, X])

sprite = {puzzle[y][2]: puzzle[y][3] for y in range(len(puzzle))}
sprite[0] = 1

for b in range(500):
    if b not in sprite and b != 0:
        sprite[b] = sprite[b-1]
    else:
        sprite[b] = sprite[b]
    
for c in range(6):
    offset = c * 40
    c += 1
    for d in range(40):
        if d == sprite[d + offset] or d == sprite[d + offset] - 1 or d == sprite[d + offset] + 1:
            print('#', end='')
        else:
            print('.', end='')
    print('')