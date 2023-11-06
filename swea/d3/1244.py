t = int(input())
def dfs(nowlist,cnt):
    global ans
    if k == cnt:
        ans = max(ans, int(''.join(nowlist)))
        return
        
        
    for i in range(len(numlist)-1):
        for j in range(i+1, len(numlist)):
                nowlist[i], nowlist[j] = nowlist[j], nowlist[i]
                if int(''.join(nowlist))+cnt not in visited:
                    visited.append(int(''.join(nowlist))+cnt)
                    dfs(nowlist,cnt+1)
                nowlist[i], nowlist[j] = nowlist[j], nowlist[i]
for tc in range(1,t+1):
    visited = []
    ans = 0
    num, k = map(str,input().split())
    numlist = list(num)
    k = int(k)
    dfs(numlist,0)
    print(f"#{tc} {ans}")