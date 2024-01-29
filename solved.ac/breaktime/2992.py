import sys
num = sys.stdin.readline().rstrip()
numList = list(num)
num = int(num)
visited = [False] * len(numList)
ans = []

result = []
def back():
    if len(result) == len(numList):
        if num < int(''.join(result)):
            ans.append(int(''.join(result)))
        return
    for i in range(len(numList)):
        if visited[i] == False:
            result.append(numList[i])
            visited[i] = True
            back()
            result.pop()
            visited[i] = False

back()
if ans:
    print(min(ans))
else:
    print(0)
