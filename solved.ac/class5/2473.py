import sys
n = int(sys.stdin.readline())
water = list(map(int,sys.stdin.readline().split()))
water.sort()

ans = [water[0],water[1],water[n-1]]
result = abs(water[0] + water[1] + water[n-1])
for i in range(n):
    start = 0
    end = n-1
    while start < end:
        if start == i:
            start += 1
            end = n-1
            continue
        if end == i:
            end -= 1
            continue
        if result > abs(water[i] + water[start] + water[end]):
            ans = []
            result = abs(water[i] + water[start] + water[end])
            ans = [water[i], water[start], water[end]]
        if water[i] + water[start] + water[end] > 0:
            end -= 1
        else:
            start += 1
ans.sort()
print(*ans)