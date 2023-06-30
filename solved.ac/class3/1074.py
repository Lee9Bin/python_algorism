import sys
N, r, c = map(int, sys.stdin.readline().split())

def dfs(x,y,N):
    global cnt
    # print(cnt)
    # 1사분면
    if x < N//2 and y<N//2:
        if N == 2:
            print(cnt)
            return
        # print("1사분면")
        dfs(x,y,N//2)
    # 2사분면
    elif x < N//2 and y>=N//2:
        if N == 2:
            print(cnt+1)
            return
        # print("2사분면")
        cnt = cnt + (N//2)*(N//2)*1
        dfs(x,y-N//2,N//2)
    # 3사분면
    elif x >= N//2 and y<N//2:
        if N == 2:
            print(cnt+2)
            return
        # print("3사분면")
        cnt = cnt + (N//2)*(N//2)*2

        dfs(x-N//2,y,N//2)
    # 4사분면
    elif x >=N//2 and y>=N//2:
        if N == 2:
            print(cnt+3)
            return
        # print("4사분면")
        cnt = cnt + (N//2)*(N//2)*3
        dfs(x-N//2,y-N//2,N//2)
    

cnt = 0
dfs(r,c,2**(N))