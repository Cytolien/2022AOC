with open('1.txt') as f:
    elves = [ int(x.strip() or 0) for x in f.readlines() ]
    
calories = []
sum_calories = 0

for a in elves:
    if a != 0:
        sum_calories += a
    else:
        calories.append(sum_calories)
        sum_calories = 0

print(sum(sorted(calories, reverse=True)[:3]))