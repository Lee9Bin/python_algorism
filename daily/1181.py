import sys

n = int(sys.stdin.readline())
alpha = [[] for i in range(51)]
for i in range(n):
    x = sys.stdin.readline().rstrip()
    if x not in alpha[len(x)]:
        alpha[len(x)].append(x)

for i in alpha:
    i.sort()
    for j in i:
        print(j)
