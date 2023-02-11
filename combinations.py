import itertools


n = int(input('print N:'))
alphabet = 'abcdefghijklmnopqrstuvwxyz'[:n]
answer = []


for i in range(n + 1):
    for combination in itertools.combinations(alphabet, i):
        answer.append(''.join(combination))
answer.sort()
print(' '.join(answer))
