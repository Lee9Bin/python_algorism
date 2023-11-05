t = int(input())

for tc in range(1,t+1):
    n = int(input())
    
    numlist = list(map(int,input().split()))
    up, down = 0, 0
    current = numlist[0]
    for i in range(1,n):
        if current < numlist[i]:
            up = max(up,numlist[i]-current)
        else:
            down = max(up,current-numlist[i])
        current = numlist[i]
    print(f"#{tc} {up} {down}")