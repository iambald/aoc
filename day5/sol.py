input = open('input.txt', 'r').read().split('\n')

vowels = ['a', 'e', 'i', 'o', 'u']
prohibited = ['ab', 'cd', 'pq', 'xy']

nice = 0
for string in input:
    if (sum(map(lambda v: string.count(v), vowels)) >= 3 and
        sum(map(lambda p: string.count(p), prohibited)) == 0 and
        sum(map(lambda s: 1 if s[0] == s[1] else 0, zip(string, string[-1:] + string[:-1])[1:])) > 0):
        nice += 1

print nice
