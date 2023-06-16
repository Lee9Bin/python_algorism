import sys
N, M = map(int, sys.stdin.readline().split())
color = list()
for _ in range(M):
    i = int(sys.stdin.readline())
    color.append(i)
result = list()
left = 1
right = max(color)

while left <= right:
    mid = (left+right)//2
    students = 0
    for i in color:
        if i % mid == 0:
            students += i//mid
        else:
            students += (i//mid) + 1
    if students <=N:
        result.append(mid)
        right = mid-1
    else:
        left = mid +1

print(min(result))