import sys
n = int(sys.stdin.readline())

origin = [[1,1],[1,0]]
a = [[1,0],[0,1]]

def multy(o1,o2):
    ret = [[0,0], [0,0]]
    ret[0][0] = ((o1[0][0] * o2[0][0]) + (o1[0][1] * o2[1][0]))%1000000007
    ret[0][1] = ((o1[0][0] * o2[0][1]) + (o1[0][1] * o2[1][1]))%1000000007
    ret[1][0] = ((o1[1][0] * o2[0][0]) + (o1[1][1] * o2[1][0]))%1000000007
    ret[1][1] = ((o1[1][0] * o2[0][1]) + (o1[1][1] * o2[1][1])) %1000000007
    return ret

while n>0:
    if n % 2 == 1:
        a = multy(a,origin)
    origin = multy(origin ,origin)

    n  = n//2

print(a[0][1])