import sys

def DFS(x,y):
    global cnt
    if x <= -1 or y <= -1 or x>=n or y>=n:
        return
    if house[x][y] == 1:
        house[x][y] = -1
        cnt +=1
        DFS(x-1,y)
        DFS(x+1,y)
        DFS(x,y-1)
        DFS(x,y+1)
    
n = int(sys.stdin.readline())
house = []
for i in range(n):
    house.append(list(map(int,sys.stdin.readline().strip())))
result = list()
cnt = 0
dnage = 0

for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            DFS(i,j)
            result.append(cnt)
            cnt=0
            dnage += 1
print(dnage)
result.sort()
for i in result:
    print(i)