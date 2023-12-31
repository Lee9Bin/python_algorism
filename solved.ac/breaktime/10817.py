import sys

numlist = list(map(int, sys.stdin.readline().split()))

numlist.sort()

print(numlist[1])