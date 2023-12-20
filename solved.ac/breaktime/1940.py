import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

numlist = list(map(int, sys.stdin.readline().split()))

numlist.sort()

start = 0
end = n-1
ans = 0
while start < end:
    if numlist[start] + numlist[end] > m:
        end -= 1
    elif numlist[start] + numlist[end] == m:
        ans +=1
        start += 1
    else:
        start +=1
        end = n-1
print(ans)