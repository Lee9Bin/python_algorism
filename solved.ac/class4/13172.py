import sys
import math
def multy(n,x):
    if x == 1:
        return n
    if x % 2 == 1:
        return n*multy(n,x-1)% mod
    temp = multy(n,x//2)
    return temp * temp % mod

m = int(sys.stdin.readline())
mod = 1000000007
result = 0
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    g = math.gcd(a,b)
    a = a//g
    b = b//g
    result += b * multy(a,mod-2) % mod
    result = result % mod
print(result)