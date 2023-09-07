import sys
n = int(sys.stdin.readline())
numlist = list(map(int,sys.stdin.readline().split()))
result = []
visited = [0] * n
ans = 0
def back():
    global ans
    if len(result) == n:
        temp = 0
        for i in range(n-1):
            temp += abs(result[i]-result[i+1])
        if temp > ans:
            ans = temp
        return 

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            result.append(numlist[i])
            back()
            visited[i] = 0
            result.pop()
back()
print(ans)