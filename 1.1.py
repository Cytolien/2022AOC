with open('1.txt') as f:
    elves = [ x.strip() for x in f.readlines() ]
    
calories = []
sum_calories = 0

for a in elves:
    if a != '':
        sum_calories += int(a)
    else:
        calories.append(sum_calories)
        sum_calories = 0
        
print(max(calories))