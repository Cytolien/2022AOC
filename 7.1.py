import re
with open('7.txt', 'r') as f:
    puzzle = [x.strip() for x in f.readlines()]

directories = {'/': 0}
currentDir = ''
for a in puzzle:
    if '$ cd' in a and '..' not in a and '/' not in a:
        if len(currentDir) == 1:
            directories[currentDir + a.split()[-1]] = 0
            currentDir = currentDir + a.split()[-1]
        else:
            directories[currentDir + '/' + a.split()[-1]] = 0
            currentDir = currentDir + '/' + a.split()[-1]
    elif '$ cd /' in a:
        currentDir = '/'
    elif 'cd ..' in a:
        currentDir = '/'.join(currentDir.split('/')[:-1])
    elif a[0].isdigit():
        recursive = currentDir
        directories['/'] += int(re.sub('[^0-9]', '', a))
        while recursive != '/':
            directories[recursive] += int(re.sub('[^0-9]', '', a))
            recursive = '/'.join(recursive.split('/')[:-1])
            if recursive == '':
                recursive = '/'
    
answer = 0
for c in directories:
    if directories[c] <= 100000:
        answer += directories[c]
print(answer)