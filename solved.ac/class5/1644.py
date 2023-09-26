import sys
prim = [True] * 4000001

for i in range(2,int(4000001**0.5)+1):
    if prim[i] == True:
        for j in range(i+i,4000001,i):
            prim[j] = False
result = []
for i in range(2,4000001):
    if prim[i] == True:
        result.append(i)

n = int(sys.stdin.readline())
start = 0
end = 0
cnt = 0
ans= 0
while end<len(result):
    if result[end] > n:
        break
    ans += result[end]

    if ans < n:
        end += 1
    
    else:
        if ans == n:
            cnt += 1
        start +=1
        ans = 0
        end = start
print(cnt)