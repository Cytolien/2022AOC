with open('8.txt', 'r') as f:
    puzzle = [[*map(int, x.strip())] for x in f.readlines()]

def heightCheck(row, column, height):
    sides = 0
    lrow = row
    while lrow != 0:
        lrow -= 1
        if puzzle[lrow][column] >= height:
            sides += 1
            break
    rrow = row
    while rrow != len(puzzle[row])-1:
        rrow += 1
        if puzzle[rrow][column] >= height:
            sides += 1
            break
    dcolumn = column
    while dcolumn != 0:
        dcolumn -= 1
        if puzzle[row][dcolumn] >= height:
            sides += 1
            break
    ucolumn = column
    while ucolumn != len(puzzle)-1:
        ucolumn += 1
        if puzzle[row][ucolumn] >= height:
            sides += 1
            break

    if sides != 4:
        return 'visible'
    
visible = 0
for a in range(len(puzzle)):
    for b in range(len(puzzle[a])):
        if a == 0 or a == len(puzzle[a])-1 or b == 0 or b == len(puzzle)-1:
            visible += 1
        elif heightCheck(a, b, puzzle[a][b]) == 'visible':
            visible += 1
            
print(visible)