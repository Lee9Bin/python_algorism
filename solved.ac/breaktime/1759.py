import sys

def back(start):
    if len(result) == l:
        checkM = 0
        checkG = 0
        for i in result:
            if i in ("a", "e", "i", "o", "u"):
                checkM += 1
            else:
                checkG += 1
        if checkM >= 1 and checkG >= 2:
            print(''.join(result))
        return
    
    for i in range(start, c):
        result.append(alphaList[i])
        back(i+1)
        result.pop()

l, c = map(int, sys.stdin.readline().split())
alphaList = list(map(str, sys.stdin.readline().split()))
alphaList.sort()

result = []
back(0)