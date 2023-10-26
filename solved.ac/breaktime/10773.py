import sys
n = int(sys.stdin.readline())
result = []
for i in range(n):
    nownum = int(sys.stdin.readline())

    if nownum == 0:
        if len(result) > 0:
            result.pop()
    else:
        result.append(nownum)
print(sum(result))