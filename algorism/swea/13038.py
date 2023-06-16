# 6 32
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    day = list(map(int, input().split()))
    ans = 100000000
    for i in range(7):
        if day[i] == 1:
            days = 0
            cnt = 0
            start = i
            while True:
                for j in day[start:]:
                    days += 1
                    if j == 1:
                        cnt +=1
                    if cnt == n:
                        break
                if cnt == n:
                    break
                start = 0
            if days < ans:
                ans= days
    print(f"#{test_case} {ans}")