import sys

t = int(sys.stdin.readline())

def dfs(start):
    global ans
    if len(three) == 3:
        cnt = 0
        for i in range(2):
            for j in range(i+1,3):
                if three[i][0] != three[j][0]:
                    cnt +=1
                if three[i][1] != three[j][1]:
                    cnt +=1
                if three[i][2] != three[j][2]:
                    cnt +=1
                if three[i][3] != three[j][3]:
                    cnt +=1
        if ans > cnt:
            ans = cnt
        return
    
    for i in range(start,n):
        three.append(mbti[i])
        dfs(i+1)
        three.pop()

for _ in range(t):
    n = int(sys.stdin.readline())
    if n >=33:
        ans = 0
        mbti = list(map(str, sys.stdin.readline().split()))
    else:
        mbti = list(map(str, sys.stdin.readline().split()))
        three = []
        ans = 1e9
        dfs(0)
    print(ans)