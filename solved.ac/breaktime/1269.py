import sys
a, b = map(int,sys.stdin.readline().split())
alist = list(map(int,sys.stdin.readline().split()))
blist = list(map(int,sys.stdin.readline().split()))

adic ={}
bdic ={}

for i in alist:
    adic[i] = 1
for i in blist:
    bdic[i] = 1
print(adic)
aAns = 0
bAns = 0

for i in alist:
    if i not in bdic:
        aAns +=1
for i in blist:
    if i not in adic:
        bAns += 1
print(aAns+bAns)