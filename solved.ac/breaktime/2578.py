import sys
def checkBingo(x,y):
    global bingo
    
    rowCnt = 0
    columnCnt = 0
    #가로 #세로
    for i in range(5):
        if visited[x][i] == True:
            rowCnt += 1
        if visited[i][y] == True:
            columnCnt += 1
    if rowCnt == 5:
        bingo +=1
    if columnCnt == 5:
        bingo += 1
    
    cnt = 0
    if x == y:
        for i in range(5):
            if visited[i][i] == True:
                cnt += 1
    if cnt == 5:
        bingo += 1
    cnt = 0
    if x + y == 4:
        for i in range(5):
            if visited[4-i][i] == True:
                cnt += 1
    if cnt == 5:
        bingo += 1
# 숫자의 좌표값 저장 -> 딕셔너리 why? 검색에 용이
dic = {}
visited = [[False for i in range(5)] for i in range(5)]

for x in range(5):
    nowList = list(map(int, sys.stdin.readline().split()))
    for y in range(5):
        dic[nowList[y]] = (x,y)

ans = []

for i in range(5):
    ans.append(list(map(int, sys.stdin.readline().split())))

cnt = 0
bingo = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        nowx, nowy = dic[ans[i][j]]
        visited[nowx][nowy] = True
        checkBingo(nowx,nowy)
        if bingo >=3:
            print(cnt)
            break
    if bingo >= 3:
        break