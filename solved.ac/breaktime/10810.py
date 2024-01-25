import sys
ans = []

while True:
    s = sys.stdin.readline().rstrip()
    if s == "":
        break
    ans.append(s)

for i in ans:
    print(i)