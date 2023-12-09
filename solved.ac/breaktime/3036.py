import sys
n = int(sys.stdin.readline())
numlist = list(map(int, sys.stdin.readline().split()))

def gcd(a,b):
    
    while b > 0:
        a, b = b, a % b
        
    return a

for i in range(1,n):
    ans = gcd(numlist[0],numlist[i])
    print(f"{numlist[0]//ans}/{numlist[i]//ans}")
    