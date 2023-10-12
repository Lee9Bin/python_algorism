import sys
numlist = list(sys.stdin.readline().rstrip())
numlist.sort(reverse=True)
print(''.join(numlist))