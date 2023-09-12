import sys
n = int(sys.stdin.readline())
card = [0] * 1000001
result =[0] * 1000001
nlist = list(map(int,sys.stdin.readline().split()))

for i in nlist:
    card[i] = 1

maxnum = max(nlist)

for i in nlist:
    for j in range(i*2,maxnum+1,i):
        if card[j] == 1:
            result[i] += 1
            result[j] -=1

for i in nlist:
    print(result[i],end=" ")
print()