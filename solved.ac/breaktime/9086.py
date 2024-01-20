import sys
n = int(sys.stdin.readline())

for i in range(n):
    ans = sys.stdin.readline().rstrip()
    print(ans[0]+ans[-1])