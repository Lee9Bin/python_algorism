for tc in range(1,11):
    t = int(input())
    n,m = map(int,input().split())

    ans = 1

    for i in range(m):
        ans *= n
    
    print(f"#{tc} {ans}")