boxes = filter(lambda box: len(box) == 3, map(lambda box: map(lambda num: num if num == "" else int(num), box.split('x')), open('input.txt', 'r').read().split('\n')))

paper = 0
for box in boxes:
    mult = map(lambda (a, b): a*b, zip(box, box[-1:]+box[:-1]))
    paper += 2*sum(mult) + min(mult)
print paper
