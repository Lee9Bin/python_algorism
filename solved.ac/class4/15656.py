import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())

chicken = []
for i in range(n):
    chicken.append(list(map(int,sys.stdin.readline().split())))

homes =[]
chicks =[]
for i in range(n):
    for j in range(n):
        if chicken[i][j] == 1:
            homes.append([i,j]) 
        if chicken[i][j] == 2:
            chicks.append([i,j])

def back(start):
    global result
    if len(select) == m:
        sums = 0
        for r1,c1 in homes:
            now=abs(r1-select[0][0]) + abs(c1-select[0][1])
            for r2,c2 in select:
                if now > abs(r1-r2) + abs(c1-c2):
                    now = abs(r1-r2) + abs(c1-c2)
            sums += now
        if sums < result:
            result = sums
        return
    for i in range(start,len(chicks)):
        select.append(chicks[i])
        back(i+1)
        select.pop()
result = 1e9
select = []
back(0)
print(result)
