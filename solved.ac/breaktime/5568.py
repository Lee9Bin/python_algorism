import sys
def back():
    if len(now) == k:
        if ''.join(now) not in result:
            result.append(''.join(now))
        return
    
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            now.append(numlist[i])
            back()
            visited[i] = False
            now.pop()

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
numlist = []

for i in range(n):
    numlist.append(sys.stdin.readline().rstrip())
result = []
ans = 0
now = []
visited = [False] * n
back()
print(len(result))