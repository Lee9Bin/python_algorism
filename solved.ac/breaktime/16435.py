import sys
n, m = map(int,sys.stdin.readline().split())
numlist = list(map(int,sys.stdin.readline().split()))
numlist.sort()
for i in range(n):
    if m>= numlist[i]:
        m+=1
print(m)