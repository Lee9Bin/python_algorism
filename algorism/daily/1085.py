import sys

result = []

while True:
    numlist = list(map(int, sys.stdin.readline().split()))
    if numlist.count(0) == 3:
        break
    numlist.sort(reverse=True)
    if numlist[0] ** 2 == numlist[1] ** 2 + numlist[2] ** 2:
        result.append("right")
    else:
        result.append("wrong")
for i in result:
    print(i)
