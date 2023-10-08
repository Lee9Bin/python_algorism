import sys
s = sys.stdin.readline().rstrip()

result = []
for i in range(len(s)):
    result.append(s[i:])
result.sort()

for k in result:
    print(k)