import sys
T = int(sys.stdin.readline())

for t in range(T):
    AC = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()
    numlist = []
    a = []
    for i in arr:
        if i != '[' and i != ']' and i !=',':
            a.append(i)
        else:
            if len(a) > 0:
                numlist.append(int(''.join(map(str,a))))
            a=[]
    rcnt = 0
    flag = 0
    for j in AC:
        if j == 'R':
            rcnt += 1
        elif j == "D":
            if len(numlist)==0:
                    flag = 1
                    break
            if rcnt % 2 == 0:
                    numlist.pop(0)
            elif rcnt % 2 == 1:
                    numlist.pop()
    
    if flag == 0:
        if rcnt % 2 == 1: 
            numlist.reverse()
        print('[',end='')
        for i in range(len(numlist)):
            if i == len(numlist)-1:
                print(numlist[i],end='')
            else:
                print(numlist[i],end=",")
        print(']')
    elif flag == 1:
        print('error')