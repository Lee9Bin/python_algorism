import sys
n, m = map(int,sys.stdin.readline().split())

six, one = 1e9, 1e9

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    six = min(six, a)
    one = min(one, b)


if six < (one * 6):
    if six < (n%6)*one:
        print((n//6+1)*six)
    else:
        print((n//6)*six + (n%6)*one)
else:
    print(n*one)