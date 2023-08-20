import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

bdp = [1] *(n)
sdp =[1] *(n)
for i in range(n):
    for j in range(i,n):
        if a[i] < a[j]: # 커지는
            bdp[j] = max(bdp[i]+1,bdp[j])
        if a[n-1-i] < a[n-1-j]: # 작아지는
            sdp[n-j-1] = max(sdp[n-i-1]+1,sdp[n-j-1])
result = 0
for i in range(n):
    if result < bdp[i]+sdp[i] -1:
        result = bdp[i]+sdp[i] -1
print(result)