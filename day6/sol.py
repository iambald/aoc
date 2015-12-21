import re

input = open('input.txt', 'r').read().split('\n')

grid = [[-1 for n in range(1001)] for m in range(1001)]

for line in input:
    coords = [int(s) for s in re.split('[ ,]', line) if s.isdigit()]
    command = 0
    if 'on' in line:
        command = 0
    elif 'off' in line:
        command = 1
    elif 'toggle' in line:
        command = 2
    if len(coords) == 4:
        for x in range(coords[0], coords[2]+1):
            for y in range(coords[1], coords[3]+1):
                grid[x][y] = 1 if command == 0 else -1 if command == 1 else -1*grid[x][y]


sum = 0
for x in range(1001):
    for y in range(1001):
        if grid[x][y] > 0: sum+=1

print sum
