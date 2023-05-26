# 
T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    point = list(map(int, input().split()))
    point.sort(reverse=True)
    
    print(f"#{test_case} {sum(point[:m])}")