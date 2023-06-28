import sys

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
sublist = sorted(nlist)

dic ={}
cnt = 0
for i in range(n):
    if sublist[i] not in dic:
        dic[sublist[i]] = cnt
        cnt +=1
print(dic)
for i in nlist:
    print(dic[i],end=' ')