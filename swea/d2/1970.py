t = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1,t+1):
    n = int(input())
    result = [0,0,0,0,0,0,0,0]
    nowMoney = 0
    
    while n >= 10:
        result[nowMoney] = n//money[nowMoney]
        n %= money[nowMoney]
        nowMoney += 1
    print(f"#{tc}")
    print(*result)