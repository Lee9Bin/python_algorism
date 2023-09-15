import sys
sdoqu = [[] for i in range(9)]
zero = []
for i in range(9):
    nlist = sys.stdin.readline().strip()
    for k in nlist:
        sdoqu[i].append(int(k))

for i in range(9):
    for j in range(9):
        if sdoqu[i][j] == 0:
            zero.append((i,j))

def check(x,y):
    poss = [1,2,3,4,5,6,7,8,9]

    #행  
    for i in range(9):
        try:
            poss.remove(sdoqu[x][i])
        except:
            continue
    
    for i in range(9):
        try:
            poss.remove(sdoqu[i][y])
        except:
            continue
    
    for i in range(x//3*3,x//3*3+3):
        for j in range(y//3*3,y//3*3+3):
            try:
                poss.remove(sdoqu[i][j])
            except:
                continue
    return poss

def back():

for a,b in zero:
    possible = check(a,b)
    for i in possible:
        sdoqu[i][j] = i
        back()
        sdoqu[i][j] = 0


# 0인 부분을 찾는다.
# 각 행 각 열 각 행정구역을 판단한 가능한 숫자를 뽑아낸다.
# 뽑은 리스트틀 가지고 백트래킹을 진행한다.