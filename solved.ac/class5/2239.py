import sys
sdoqu = []
zero = []
for i in range(9):
    sdoqu.append(list(map(str,sys.stdin.readline().strip())))

for i in range(9):
    for j in range(9):
        if sdoqu[i][j] == '0':
            zero.append((i,j))

def check(x,y,k):

    #행  
    for i in range(9):
        if sdoqu[x][i] == k:
            return False
    
    # 열
    for i in range(9):
        if sdoqu[i][y] == k:
            return False
    
    # 격자
    for i in range(x//3*3,x//3*3+3):
        for j in range(y//3*3,y//3*3+3):
            if sdoqu[i][j] == k:
                return False
    return True

def back(depth):
    if depth == len(zero):
        for k in range(9):
            print(''.join(sdoqu[k]))
        exit(0)
    
    for i in range(1,10):
        x = zero[depth][0]
        y = zero[depth][1]
        
        if check(x,y,str(i)):
            sdoqu[x][y] = str(i)
            back(depth + 1)
            sdoqu[x][y] = 0

back(0)