import sys
def back(start):
    if len(result) == 6:
        print(*result)
        return
    
    for i in range(start,nlist[0]+1):
        result.append(nlist[i])
        back(i+1)
        result.pop()


while True:
    nlist = list(map(int,sys.stdin.readline().split()))
    if nlist[0] == 0:
        break
    result = []
    back(1)
    print()
