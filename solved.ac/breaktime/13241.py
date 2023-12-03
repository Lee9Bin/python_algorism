import sys
# 일단 공차 K랑 차이가 가장 작은것은 찾자
def GCD(x, y):
    while y > 0:
        x, y = y, x % y
    return x
a, b = map(int, sys.stdin.readline().split())

print(a*b//GCD(a,b))