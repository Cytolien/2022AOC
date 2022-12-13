import math
with open('9.txt', 'r') as f:
    puzzle = [x.strip().split() for x in f.readlines()]

def follow(tail, head):
    if (tail[0]==head[0] or tail[0]+1==head[0] or tail[0]-1==head[0]) and (tail[1]==head[1] or tail[1]+1==head[1] or tail[1]-1==head[1]):
        return tail
    else:
        ans = [0,0]
        if head[0]-tail[0] == -1:
            ans[0] = head[0]-tail[0]+tail[0]
        else:
            ans[0] = math.ceil((head[0]-tail[0])/2)+tail[0]
        if head[1]-tail[1] == -1:
            ans[1] = head[1]-tail[1]+tail[1]
        else:
            ans[1] = math.ceil((head[1]-tail[1])/2)+tail[1]
        return ans
    
coords = [[0,0]]
direction = {'R': [1,0], 'L': [-1,0], 'U': [0,1], 'D': [0,-1]}
ligaments = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

for a in puzzle:
    for b in range(int(a[1])):
        for c in range(len(ligaments)):
            if c == 0:
                ligaments[c] = [ligaments[c][0] + direction[a[0]][0], ligaments[c][1] + direction[a[0]][1]]
            else:
                ligaments[c] = follow(ligaments[c], ligaments[c-1])
                
            if c == 9 and ligaments[c] not in coords:
                coords.append(ligaments[c])

print(len(coords))