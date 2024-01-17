import sys
n = int(sys.stdin.readline())

dic = {}
ans = 0

for i in range(n):
    now = sys.stdin.readline().rstrip()
    
    if (now == "ENTER"):
        dic.clear()
    
    else:
        if now not in dic:
            dic[now] = 1
            ans +=1
print(ans)