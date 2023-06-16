import sys
n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
nlist.sort()
dic ={}
for i in nlist:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

m = int(sys.stdin.readline())
mlist = list(map(int, sys.stdin.readline().split()))

for i in mlist:
    if i in dic:
        print(dic[i],end=' ')
    else:
        print(0,end=' ')