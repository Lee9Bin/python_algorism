import sys

n = int(sys.stdin.readline())
human = []

for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    human.append([int(age), name])
human.sort(key=lambda x: x[0])

for i in human:
    print(*i)
