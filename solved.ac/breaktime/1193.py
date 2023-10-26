import sys
x = int(sys.stdin.readline())
numlist = []

total = 0
start = 0
for i in range(1,10000001):
    if total < x:
        total += i
        start = i
    else:
        total -= (i-1)
        start = i-1
        break

# print(total,start)

for i in range(x-total):
    if start % 2 == 0:
        if x-total-1 == i:
            print(str(i+1)+"/"+str(start-i))
    else:
        if x-total-1 == i:
            print(str(start-i)+"/"+str(i+1))