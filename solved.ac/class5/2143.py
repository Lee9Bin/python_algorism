import sys
T = int(sys.stdin.readline())

n = int(sys.stdin.readline())
nlist = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
mlist = list(map(int,sys.stdin.readline().split()))

ndp = {}
mdp = {}

for i in range(n):
    for j in range(i+1,n+1):
        if sum(nlist[i:j]) not in ndp:
            ndp[sum(nlist[i:j])] = 1
        else:
            ndp[sum(nlist[i:j])] = ndp.get(sum(nlist[i:j])) + 1
for i in range(m):
    for j in range(i+1,m+1):
        if sum(mlist[i:j]) not in mdp:
            mdp[sum(mlist[i:j])] = 1
        else:
            mdp[sum(mlist[i:j])] = mdp.get(sum(mlist[i:j])) + 1
ans = 0
for key in ndp.keys():
    try:
        ans += ndp[key] * mdp[T-key]
    except:
        continue
print(ans)
