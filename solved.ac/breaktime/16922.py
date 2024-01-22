import sys
def back(start,cnt,total):
    if cnt >= n:
        if cnt == n and total not in ans:
            ans.append(total)  
        return
    
    for i in range(start,4):
        back(i,cnt+1, total+loma[i])

n = int(sys.stdin.readline())
loma = [1,5,10,50]
ans = []
back(0,0,0)
print(len(ans))
