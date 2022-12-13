with open('10.txt', 'r') as f:
    puzzle = [x.strip().split() for x in f.readlines()]

cycle = 0
X = 1
answers = [20, 60, 100, 140, 180, 220]
answer = 0
for a in range(len(puzzle)):
    if len(puzzle[a]) == 1:
        cycle += 1
        puzzle[a].extend([0, cycle, X])
    else:
        cycle += 2
        X += int(puzzle[a][1])
        puzzle[a].extend([cycle, X])
        
    if cycle + 1 in answers:
        answer += answers.pop(0) * X
        print(answer)
    elif cycle in answers:
        print(answer)
        answer += answers.pop(0) * puzzle[a-1][3]
        print(answer)