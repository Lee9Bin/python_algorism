import sys

n = int(sys.stdin.readline())
plus = 0
dienum = 666
result = [666]
while True:
    if len(result) == n:
        break
    dienum += 1
    if "666" in str(dienum):
        result.append(dienum)
    plus += 1

print(result[n - 1])
