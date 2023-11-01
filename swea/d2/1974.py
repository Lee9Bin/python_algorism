
#행 판단
def rowCheck(x,graph):
    checkList = []
    for i in range(9):
        if graph[x][i] in checkList:
            return 1
        else:
            checkList.append(graph[x][i])
    return 0

#열 판단
def colCheck(y,graph):
    checkList = []
    for i in range(9):
        if graph[i][y] in checkList:
            return 1
        else:
            checkList.append(graph[i][y])
    return 0

#3*3판단
def threeCheck(x,y,graph):
    checkList = []
    for i in range(x//3*3, x//3*3+3):
        for j in range(y//3*3, y//3*3+3):
            if graph[i][j] in checkList:
                return 1
            else:
                checkList.append(graph[i][j])
    return 0

t = int(input())

for tc in range(1,t+1):
    sdoqu = []
    result = []
    for i in range(9):
        sdoqu.append(list(map(int,input().split())))
    
    for i in range(9):
        for j in range(9):
            result.append(rowCheck(i,sdoqu))
            result.append(colCheck(j,sdoqu))
            result.append(threeCheck(i,j,sdoqu))

    if 1 in result:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} 1")
