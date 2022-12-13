with open('9.txt', 'r') as f:
    puzzle = [x.strip().split() for x in f.readlines()]

def follow(tail, head, last_head):
    if (tail[0]==head[0] or tail[0]+1==head[0] or tail[0]-1==head[0]) and (tail[1]==head[1] or tail[1]+1==head[1] or tail[1]-1==head[1]):
        return tail
    else:
        return last_head

coords = [[0,0]]
direction = {'R': [1,0], 'L': [-1,0], 'U': [0,1], 'D': [0,-1]}
head = [0,0]
tail = [0,0]
for a in puzzle:
    for b in range(int(a[1])):
        last_head = head
        head = [head[0] + direction[a[0]][0], head[1] + direction[a[0]][1]]
        tail = follow(tail, head, last_head)
        if tail not in coords:
            coords.append(tail)

print(len(coords))