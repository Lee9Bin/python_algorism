import sys
k, n = map(int,sys.stdin.readline().split())
lan = []
for i in range(k):
    lan.append(int(sys.stdin.readline()))

lan.sort()

fisrt = 0
last = lan[-1]
result = 0
while fisrt <= last:
    sum = 0
    mid = (fisrt+last)//2
    for i in lan:
        sum += i//mid
    if sum >= n:
        fisrt = mid +1
        if result < mid:
            result = mid
    else:
        last = mid-1
print(result)