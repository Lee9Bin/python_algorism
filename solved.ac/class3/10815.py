import sys
n = int(sys.stdin.readline())
numdic = {}

numlist = list(map(int,sys.stdin.readline().split()))
for i in numlist:
    numdic[i] = 1
    
m = int(sys.stdin.readline())
numlist = list(map(int,sys.stdin.readline().split()))

for i in numlist:
    if i not in numdic:
        print(0,end=' ')
    else:
        print(numdic[i],end=' ')