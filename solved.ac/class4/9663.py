import sys
n = int(sys.stdin.readline())

def back(depth):
    global cnt
    if depth == n:
        cnt +=1
        return
    
    # 다음 좌표 depth,i
    for i in range(n):
        flag = True
        for a,b in queen:
            if i == b or (abs(depth-a) == abs(i-b)):
                flag = False
                break
        if flag == True:
            queen.append((depth,i))
            back(depth+1)
            queen.pop()
queen = []
cnt = 0
for i in range(n):
    queen.append((0,i))
    back(1)
    queen.pop()
print(cnt)