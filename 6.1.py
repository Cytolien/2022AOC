with open('6.txt') as f:
    puzzle = [x for x in f.readlines()]

count = 0
temp = []
answer = []
for a in puzzle[0]:
    if count >= 4:
        if len(set(temp)) == len(temp):
            answer.append(count)
        else:
            temp.pop(0)
    temp.append(a)    
    count += 1
    
print(min(answer))