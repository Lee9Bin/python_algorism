import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
tree.sort()

start = 0
end = tree[-1]
ans = 0
while start<=end:
    result = 0
    mid = (start+end)//2
    for i in tree:
        if i > mid:
            result += i-mid
    if result > m:
        start = mid+1
        if ans < mid:
            ans = mid
    elif result < m:
        end = mid-1
    else:
        ans = mid
        break
print(ans)
