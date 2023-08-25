import sys
n, m = map(int,sys.stdin.readline().split())
word = {}
ans = 0
for i in range(n):
    arr = sys.stdin.readline().rstrip()
    word[arr] = 1

for i in range(m):
    arr = sys.stdin.readline().rstrip()
    try:
        if word[arr] == 1:
            ans +=1
    except:
        continue
print(ans)