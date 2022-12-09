with open('8.txt', 'r') as f:
    puzzle = [[*map(int, x.strip())] for x in f.readlines()]

def sightCheck(row, column, height):
    ko, vex, pul, thul = 0, 0, 0, 0
    lrow = row
    while lrow != 0:
        lrow -= 1
        if puzzle[lrow][column] >= height:
            ko += 1
            break
        else:
            ko += 1
    rrow = row
    while rrow != len(puzzle[row])-1:
        rrow += 1
        if puzzle[rrow][column] >= height:
            vex += 1
            break
        else:
            vex += 1
    dcolumn = column
    while dcolumn != 0:
        dcolumn -= 1
        if puzzle[row][dcolumn] >= height:
            pul += 1
            break
        else:
            pul += 1
    ucolumn = column
    while ucolumn != len(puzzle)-1:
        ucolumn += 1
        if puzzle[row][ucolumn] >= height:
            thul += 1
            break
        else:
            thul += 1
    
    return ko * vex * pul * thul
    
scores = {}
for a in range(len(puzzle)):
    for b in range(len(puzzle[a])):
        scores[a,b] = sightCheck(a, b, puzzle[a][b])

print(max({scores[z] for z in scores}))