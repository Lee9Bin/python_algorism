import sys
n = int(sys.stdin.readline())
left = list(map(int,sys.stdin.readline().split()))
visted = [False] *n
result = [0] * n

for k in range(1,n+1):
    cnt = 0
    for i in range(n):
        if cnt == left[k-1] and visted[i] == False:
                result[i] = k
                visted[i] = True
                break
        if visted[i] == False:
            cnt += 1
        
print(result)