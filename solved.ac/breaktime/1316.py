import sys
n = int(sys.stdin.readline())
ans = 0

for i in range(n):
    word = sys.stdin.readline().rstrip()
    visited = []
    nows = word[0]
    flag = True
    for k in range(1,len(word)):
        if nows != word[k]:
            if nows not in visited:
                visited.append(nows)
                nows = word[k]
            else:
                flag =False
                break
    if nows in visited:
        flag = False
    if flag == True:
        ans +=1
print(ans)