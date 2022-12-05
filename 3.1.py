import string
with open('3.txt', 'r') as f:
    stuff = [x.strip() for x in f.readlines()]
            
splitting = [[a[:int(len(a)/2)], a[int(len(a)/2):]] for a in stuff]
letters = [a for a in string.ascii_lowercase]
[letters.append(b) for b in string.ascii_uppercase]

keys = {letters[c]: c+1 for c in range(len(letters))}

def value(wo, rd):
    for a in wo:
        if a in rd:
            return keys[a]
            
print(sum([value(d[0], d[1]) for d in splitting]))