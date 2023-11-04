t = int(input())

for tc in range(1,t+1):
    n = int(input())
    ans = 0
    numlist = list(map(int,input().split()))
    
    start = numlist[-1]
    for i in range(n-2,-1,-1):
        if start < numlist[i]:
            start = numlist[i]
        else:
            ans += start-numlist[i]
    
    print(f"#{tc} {ans}")