import sys
sen = sys.stdin.readline().rstrip()
find = sys.stdin.readline().rstrip()
start = 0
ans = 0

while start < len(sen):
    if sen[start:start+len(find)] == find:
        ans += 1
        start += len(find)
    else:
        start += 1
print(ans)