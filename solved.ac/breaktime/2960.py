import sys

n, k = map(int,sys.stdin.readline().split())
visited = [False] *(n+1)
ans = 0
for i in range(2,n+1):
    if visited[i] == False:
        visited[i] = True
        ans += 1
        if ans ==k:
            print(i)
            break
        for j in range(i,n+1,i):
            if visited[j] == False:
                visited[j] = True
                ans +=1
            if ans == k:
                print(j)
                break