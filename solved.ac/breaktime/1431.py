import sys
n = int(sys.stdin.readline())
serial = []

for i in range(n):
    serial.append(sys.stdin.readline().rstrip())
def total(x):
    result = 0
    for i in x:
        if i.isdigit():
            result += int(i)
    return result

serial.sort(key=lambda x:(len(x),total(x),x))

for i in serial:
    print(i)
