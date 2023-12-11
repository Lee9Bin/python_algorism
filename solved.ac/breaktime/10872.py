import sys
n = int(sys.stdin.readline())

result = 1

for i in range(2,n+1):
    result*=i
    
print(result)