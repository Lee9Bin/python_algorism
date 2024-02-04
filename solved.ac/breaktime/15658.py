import sys
n = int(sys.stdin.readline())
numlist = list(map(int,sys.stdin.readline().split()))
oper = list(map(int,sys.stdin.readline().split()))
maxResult = -(1e9+1)
minResult =(1e9)+1

def back(total,start):
    global maxResult
    global minResult
    if start == n:
        if maxResult <total:
            maxResult= total
        if minResult > total:
            minResult = total
        return
    if oper[0] > 0:
        oper[0] -= 1
        back(total+numlist[start],start+1)
        oper[0] += 1
        
    if oper[1] > 0:
        oper[1] -= 1
        back(total-numlist[start],start+1)
        oper[1] += 1

    if oper[2] > 0:
        oper[2] -= 1
        back(total*numlist[start],start+1)
        oper[2] += 1

    if oper[3] > 0:
        oper[3] -= 1
        if (total< 0):
            back(-((-total)//numlist[start]),start+1)
        else:
            back(total//numlist[start],start+1)

        oper[3] += 1

total = numlist[0]
back(total,1)
print(maxResult)
print(minResult)