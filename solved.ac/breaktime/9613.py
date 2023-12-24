import sys
import math

t = int(sys.stdin.readline())

for T in range(t):
    numlist = list(map(int, sys.stdin.readline().split()))
    ans = 0
    
    for i in range(1,numlist[0]+1):
        for j in range(i+1, numlist[0]+1):
            ans += math.gcd(numlist[i],numlist[j])
    print(ans)