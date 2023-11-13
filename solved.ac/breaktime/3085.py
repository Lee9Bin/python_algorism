import sys
def dfs(nowx,nowy,dx,dy,target,cnt):
    global ans
    ans = max(ans,cnt)

    if nowx+dx >= 0 and nowy + dy >= 0 and nowx+dx < n and nowy+dy < n:
        if candy[nowx+dx][nowy + dy] == target:
            dfs(nowx+dx, nowy + dy, dx,dy,target , cnt+1)


def checkLength():
    for i in range(n):
        for j in range(n):
            for k in range(2):
                dfs(i,j,dx[k],dy[k],candy[i][j],1)
    
n = int(sys.stdin.readline())
ans = 0
candy = []

for i in range(n):
    candy.append(list(map(str,sys.stdin.readline().rstrip())))

# 자리바꾼거 완료
dx = [0,1]
dy = [1,0]

for i in range(n):
    for j in range(n):


        for k in range(2):
            nextx = i + dx[k]
            nexty = j + dy[k]

            if nextx >= 0 and nexty >= 0 and nextx < n and nexty <n:
                if candy[i][j] != candy[nextx][nexty]:
                    candy[i][j], candy[nextx][nexty] = candy[nextx][nexty], candy[i][j]
                    checkLength()
                    candy[i][j], candy[nextx][nexty] = candy[nextx][nexty], candy[i][j]
print(ans)