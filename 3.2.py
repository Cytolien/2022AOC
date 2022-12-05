import string
with open('3.txt', 'r') as f:
    stuff = [x.strip() for x in f.readlines()]
            
groups = [stuff[t:t+3] for t in range(0, len(stuff), 3)]

letters = [a for a in string.ascii_lowercase]
[letters.append(b) for b in string.ascii_uppercase]

keys = {letters[c]: c+1 for c in range(len(letters))}

def value(wo, rd, too):
    for a in wo:
        if a in rd and a in too:
            return keys[a]
            
print(sum([value(d[0], d[1], d[2]) for d in groups]))