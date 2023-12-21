import sys
n = int(sys.stdin.readline())

for i in range(n):
    index, sen = map(str, sys.stdin.readline().split())
    senList = list(sen)
    senList.pop(int(index)-1)
    print(''.join(senList))