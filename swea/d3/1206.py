for i in range(10):
    n = int(input())
    building = list(map(int,input().split()))
    
    ans = 0
    for k in range(2,n-2):
        nowHeight = building[k]
        
        left = max(building[k-1],building[k-2])
        right = max(building[k+1],building[k+2])
        
        lrHeight = max(left,right)
        
        if nowHeight - lrHeight > 0:
            ans += nowHeight - lrHeight
    print(f"#{i+1} {ans}")