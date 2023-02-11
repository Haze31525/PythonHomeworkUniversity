import random

s = []
n = int(input())
for i in range(n):
    a = []
    a.append(random.randint(0, 364))
    for i in range(365):
        x = random.randint(0, 364)
        if x not in a:
            a.append(x)
        else:
            break
    s.append(len(a))
print(round(sum(s) / len(s)))
