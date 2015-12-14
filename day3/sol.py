input = open('input.txt', 'r').read()
visited = set({(0, 0)})
pos = (0, 0)

for step in input:
    pos = {
        '>': tuple(map(sum, zip(pos, (1, 0)))),
        '<': tuple(map(sum, zip(pos, (-1, 0)))),
        '^': tuple(map(sum, zip(pos, (0, -1)))),
        'v': tuple(map(sum, zip(pos, (0, 1))))
    }.get(step, pos)
    visited.update({pos})

print len(visited)
