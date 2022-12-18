with open('11.txt', 'r') as f:
    puzzle = [x.strip() for x in list(f) if x.strip() != '']
puzzle = [puzzle[y*6:y*6+6] for y in range(8)]

items = [[int(test.strip()) for test in z[1].split(':')[-1].split(',')] for z in puzzle]
operation = [z[2].split()[-2:] for z in puzzle]
test = [int(z[3].split()[-1]) for z in puzzle]
true = [int(z[4].split()[-1]) for z in puzzle]
false = [int(z[5].split()[-1]) for z in puzzle]

monkeys = {}
monkeys = {int(puzzle[x][0].split()[-1].strip(':')): {'items': items[x], 'operation': operation[x], \
    'test': test[x], 'true': true[x], 'false': false[x], 'count': 0} for x in range(len(puzzle))}

for why in range(20):
    for a in range(len(monkeys)):
        while len(monkeys[a]['items'])> 0:
            if '*' in monkeys[a]['operation'][0]:
                if (monkeys[a]['operation'][1]).isdigit():
                    monkeys[a]['items'][0] = monkeys[a]['items'][0] * int(monkeys[a]['operation'][1])
                    monkeys[a]['items'][0] = int(monkeys[a]['items'][0] / 3)
                    if (monkeys[a]['items'][0] % monkeys[a]['test']) == 0:
                        monkeys[monkeys[a]['true']]['items'].append(monkeys[a]['items'].pop(0))
                    else:
                        monkeys[monkeys[a]['false']]['items'].append(monkeys[a]['items'].pop(0))
                        
                else:
                    monkeys[a]['items'][0] = monkeys[a]['items'][0] * monkeys[a]['items'][0]
                    monkeys[a]['items'][0] = int(monkeys[a]['items'][0] / 3)
                    if (monkeys[a]['items'][0] % monkeys[a]['test']) == 0:
                        monkeys[monkeys[a]['true']]['items'].append(monkeys[a]['items'].pop(0))
                    else:
                        monkeys[monkeys[a]['false']]['items'].append(monkeys[a]['items'].pop(0))
            else:
                if (monkeys[a]['operation'][1]).isdigit():
                    monkeys[a]['items'][0] = monkeys[a]['items'][0] + int(monkeys[a]['operation'][1]) 
                    monkeys[a]['items'][0] = int(monkeys[a]['items'][0] / 3)              
                    if (monkeys[a]['items'][0] % monkeys[a]['test']) == 0:
                        monkeys[monkeys[a]['true']]['items'].append(monkeys[a]['items'].pop(0))
                    else:
                        monkeys[monkeys[a]['false']]['items'].append(monkeys[a]['items'].pop(0))
                        
                else:
                    monkeys[a]['items'][0] = monkeys[a]['items'][0] + monkeys[a]['items'][0]
                    monkeys[a]['items'][0] = int(monkeys[a]['items'][0] / 3)
                    if (monkeys[a]['items'][0] % monkeys[a]['test']) == 0:
                        monkeys[monkeys[a]['true']]['items'].append(monkeys[a]['items'].pop(0))
                    else:
                        monkeys[monkeys[a]['false']]['items'].append(monkeys[a]['items'].pop(0))
            monkeys[a]['count'] += 1

answer = sorted([monkeys[k]['count'] for k in monkeys])
print(answer[-1]*answer[-2])