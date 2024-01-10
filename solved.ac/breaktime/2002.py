import sys
n = int(sys.stdin.readline())

cars = {}

for i in range(n):
    carName = sys.stdin.readline().rstrip()
    cars[carName] = i+1

cnt = 0
ans = 0

for i in range(n):
    nowCar = sys.stdin.readline().rstrip()
    
    # if cars[nowCar] > i+1-cnt:
    #     cnt += 1
    #     ans += 1
    
    if cars[nowCar] > i+1:
        for carName in cars:
            if i+1 <= cars[carName] < cars[nowCar]:
                cars[carName] += 1
        ans += 1
print(ans)