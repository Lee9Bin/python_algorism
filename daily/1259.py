import sys

result = []
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    numlist = list(map(str, str(n)))
    sub = list(reversed(numlist))

    if numlist == sub:
        result.append("yes")
    else:
        result.append("no")
for i in result:
    print(i)
