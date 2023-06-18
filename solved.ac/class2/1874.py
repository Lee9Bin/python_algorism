import sys
n = int(sys.stdin.readline())

nlist = []
for i in range(n):
    nlist.append(int(sys.stdin.readline()))

ans = []
stack = []
num = 1

for i in nlist:
    while num <= i:
        stack.append(num)
        ans.append('+')
        num +=1
    if stack[-1] == i:
        stack.pop()
        ans.append('-')
    else:
        ans = 'NO'
        break
if ans == 'NO':
    print('NO')
else:
    for i in ans:
        print(i)
