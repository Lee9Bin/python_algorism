import sys

n, m = map(int, sys.stdin.readline().split())

dic1 = {}
dic2 = {}

for i in range(n):
    monster = sys.stdin.readline().rstrip()
    dic1[monster] = i+1
    dic2[i+1] = monster
for i in range(m):
    result = sys.stdin.readline().rstrip()
    if result in dic1:
        print(dic1[result])
    else:
        print(dic2[int(result)])