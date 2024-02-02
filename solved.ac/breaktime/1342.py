import sys
s = list(map(str, sys.stdin.readline().rstrip()))
visited = [False] * len(s)
sDic = set([])

def back(cnt, nows):
    if cnt == len(s):
        sDic.add(''.join(nows))
        return
    
    for i in range(len(s)):
        if nows[cnt] == s[i]:
            continue
        if visited[i] == False:
            visited[i] = True
            nows.append(s[i])
            back(cnt+1, nows)
            visited[i] = False
            nows.pop()
nows = [" "]
back(0, nows)

print(len(sDic))