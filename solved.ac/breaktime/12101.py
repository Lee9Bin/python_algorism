import sys
def back(total):
    global cnt
    if total >= n:
        if total == n:
            cnt += 1
            ans.append(list(result))
        return
    
    for i in (1,2,3):
        result.append(i)
        back(total+i)
        result.pop()
n, k = map(int,sys.stdin.readline().split())
cnt = 0

result = []
ans = []
back(0)
if len(ans) < k:
    print(-1)
else:
    for i in range(len(ans[k-1])):
        if i != len(ans[k-1])-1:
            print(ans[k-1][i],end="")
            print("+",end="")
        else:
            print(ans[k-1][i])