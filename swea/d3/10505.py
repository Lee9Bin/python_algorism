t = int(input())

for tc in range(1,t+1):
    n = int(input())
    numlist = list(map(int,input().split()))
    mid = sum(numlist)/n
    
    ans = 0
    for i in numlist:
        if i <= mid:
            ans +=1
    
    print(f"#{tc} {ans}")