import sys

n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    nlist = []
    for i in range(n):
        nlist.append(int(sys.stdin.readline()))
    nlist.sort()

    gulsak = (n * 0.15)
    if gulsak - int(gulsak) >=0.5:
        gulsak = int(gulsak) +1
    else:
        gulsak = int(gulsak)
    result = sum(nlist[gulsak:n-gulsak])/(n-2*gulsak)
    if result - int(result) >= 0.5:
        print(int(result)+1)
    else:
        print(int(result))