with open('2.txt') as f:
    a = [ x.strip().split(' ') for x in f.readlines() ]
    
score = 0    

for b in a:
    choice = ''
    
    if b[1] == 'X':
        score += 0
    elif b[1] == 'Y':
        score += 3
    elif b[1] == 'Z':
        score += 6

    if b[1] == 'X':
        if b[0] == 'A':
            score += 3
        elif b[0] == 'B':
            score += 1
        elif b[0] == 'C':
            score += 2
    elif b[1] == 'Y':
        if b[0] == 'A':
            score += 1
        elif b[0] == 'B':
            score += 2
        elif b[0] == 'C':
            score += 3
    elif b[1] == 'Z':
        if b[0] == 'A':
            score += 2
        elif b[0] == 'B':
            score += 3
        elif b[0] == 'C':
            score += 1

print(score)