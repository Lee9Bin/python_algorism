import sys

n = int(sys.stdin.readline())
two = 0
five = 0
for i in range(2,n+1):
    while i % 2 == 0:
        i = i // 2
        two += 1
    while i % 5 == 0:
        i = i // 5
        five += 1

print(min(two,five))