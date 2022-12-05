with open('2.txt') as f:
    a = [ x.strip().split(' ') for x in f.readlines() ]
    
score = 0    
    
for b in a:
    if b[1] == 'X':
        score += 1
    elif b[1] == 'Y':
        score += 2
    elif b[1] == 'Z':
        score += 3

    if (b[0] == 'A' and b[1] == 'X') or (b[0] == 'B' and b[1] == 'Y') or (b[0] == 'C' and b[1] == 'Z'):
        score += 3
    elif (b[0] == 'A' and b[1] == 'Y') or (b[0] == 'B' and b[1] == 'Z') or (b[0] == 'C' and b[1] == 'X'):
        score += 6

print(score)


choice = {'X': 1, 'Y': 2, 'Z': 3}
rps = {'A': 'Rock', 'X': 'Rock', 'B': 'Paper', 'Y': 'Paper', 'C': 'Scissors', 'Z': 'Scissors'}

def winner(opp, you):
    if (opp == 'Rock' and you == 'Paper') or (opp == 'Paper' and you == 'Scissors') or (opp == 'Scissors' and you == 'Rock'):
        return 'Winner'

print(sum([choice[b[1]] for b in a]) + sum([6 if winner(z[0],z[1]) == 'Winner' else 3 if z[0]==z[1] else 0 for z in [[rps[c] for c in d] for d in a]]))