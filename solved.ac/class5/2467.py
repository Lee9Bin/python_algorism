import sys
n = int(sys.stdin.readline())
nlist = list(map(int,sys.stdin.readline().split()))
left = 0
right = n-1
result = abs(nlist[left] + nlist[right])
a = nlist[left]
b = nlist[right]
while left < right:
    if abs(nlist[left] + nlist[right]) < result:
        result = abs(nlist[left] + nlist[right])
        a,b = nlist[left],nlist[right]
    
    if nlist[left] + nlist[right] < 0:
        left +=1
    else:
        right -=1
        
print(a,b)