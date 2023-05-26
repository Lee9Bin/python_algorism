T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, l = map(int,input().split())
    food = []
    ans = 0
    for i in range(n):
        food.append(list(map(int,input().split())))

    
    def dfs(start):
        global ans
        if sum(totalcal) >= l or start == n:
            if sum(totalcal) <= l :
                if ans < sum(totallike):
                    ans = sum(totallike)
            elif sum(totalcal) > l:
                if ans < sum(totallike)-totallike[-1]:
                    ans = sum(totallike)-totallike[-1]
            return
        
        for i in range(start,n):
            if sum(totalcal) < l:
                totalcal.append(food[i][1])
                totallike.append(food[i][0])
                dfs(i+1)
                totalcal.pop()
                totallike.pop()
    
    for i in range(n):
        totalcal = []
        totallike = []
        dfs(i)
    print(f"#{test_case} {ans}")