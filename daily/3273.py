# 9
# 5 12 7 10 9 1 2 3 11
# 13

import sys
n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
nlist.sort()
x = int(sys.stdin.readline())
start = 0
end = n-1
cnt = 0
result = 0

while start < end:
    result = 0
    result = nlist[start] + nlist[end]
    if result > x:
        end -=1
    else:
        if result == x:
            cnt +=1
        start +=1
    
print(cnt)