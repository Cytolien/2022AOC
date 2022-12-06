import re
with open('5.txt') as f:
    puzzle = [x.strip() for x in f.readlines()]
    
instructions = [re.sub('[^0-9]', '', y) for y in puzzle]
stack = ['HBVWNMLP', 'MQH', 'NDBGFQML', 'ZTFQMWG', 'MTHP', 'CBMJDHGT', 'MNBFVR','PLHMRGS','PDBCN']

for a in instructions:
    times = int(a[:-2])
    take_from = int(a[-2]) - 1
    put_on = int(a[-1]) - 1
    
    stack[put_on] += stack[take_from][-times:]
    stack[take_from] = stack[take_from][:-times]

print([z[-1] for z in stack])

### Input Stack ###
# [P]     [L]         [T]            
# [L]     [M] [G]     [G]     [S]    
# [M]     [Q] [W]     [H] [R] [G]    
# [N]     [F] [M]     [D] [V] [R] [N]
# [W]     [G] [Q] [P] [J] [F] [M] [C]
# [V] [H] [B] [F] [H] [M] [B] [H] [B]
# [B] [Q] [D] [T] [T] [B] [N] [L] [D]
# [H] [M] [N] [Z] [M] [C] [M] [P] [P]
#  1   2   3   4   5   6   7   8   9 
# stack = ['HBVWNMLP', 'MQH', 'NDBGFQML', 'ZTFQMWG', 'MTHP', 'CBMJDHGT', 'MNBFVR','PLHMRGS','PDBCN']