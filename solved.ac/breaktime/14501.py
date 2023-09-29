import sys
n = int(sys.stdin.readline())
worklist = []

for i in range(n):
    worklist.append(list(map(int,sys.stdin.readline().split())))
result =[]
ans = 0
def back(nowday,total):
    global ans
    # print(result)
    # print(nowday)
    # print(total)
    if nowday <= n:
        if ans < total:
            ans = total

    for i in range(nowday,n):
        result.append(worklist[i])
        back(i+worklist[i][0],total + worklist[i][1])
        result.pop()
back(0,0)
print(ans)