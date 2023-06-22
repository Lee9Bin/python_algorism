import sys

t = int(sys.stdin.readline())
for i in range(t):
    wear = {}
    n = int(sys.stdin.readline())
    for j in range(n):
        a, b = map(str,sys.stdin.readline().split())
        if b not in wear:
            wear[b] = 1
        else:
            wear[b] +=1

# 의상중에서 안입는 경우의수1 +(의상개수)를 곱하고 하나도 선택안하는 경우 -1
    result = 1
    for k in wear:
        result *= wear.get(k)+1
    result -=1
    
    print(result)