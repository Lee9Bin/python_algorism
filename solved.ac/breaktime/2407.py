import sys
n, m = map(int, sys.stdin.readline().split())

up = 1
down = 1

for i in range(n,n-m,-1):
    up *= i
    down *= m
    m-=1

print(up//down)