import sys
n, m = map(int, sys.stdin.readline().split())
dic = {}
for i in range(n):
    name = sys.stdin.readline().rstrip()
    team = []
    for j in range(int(sys.stdin.readline())):
        team.append(sys.stdin.readline().strip())
        
    team.sort()
    dic[name] = team


for i in range(m):
    name = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    
    if n == 0:
        for j in dic[name]:
            print(j)
    else:
        for j in dic:
            if name in dic[j]:
                print(j)