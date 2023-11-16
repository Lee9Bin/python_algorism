import sys
def back(depth):
    if depth == n:
        if len(nowlist) == n+1:
            result.append(''.join(nowlist))
        return
    for i in range(10):
        if visited[i] == False and sign[depth] == "<":
            if int(nowlist[-1]) < i:
                nowlist.append(str(i))
                visited[i] = True
                back(depth+1)
                visited[i] = False
                nowlist.pop()
        if visited[i] == False and sign[depth] == ">":
            if int(nowlist[-1]) > i:
                nowlist.append(str(i))
                visited[i] = True
                back(depth+1)
                visited[i] = False
                nowlist.pop()

n = int(sys.stdin.readline())
result = []
sign = list(map(str, sys.stdin.readline().split()))

for i in range(10):
    nowlist = [str(i)]
    visited = [False]*10
    visited[i] = True
    back(0)
print(result[-1])
print(result[0])