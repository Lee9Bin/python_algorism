import sys

n, m = map(int, sys.stdin.readline().split())

homepage = {}

for i in range(n):
    page, password = map(str, sys.stdin.readline().split())
    homepage[page] = password

for j in range(m):
    nowpage = sys.stdin.readline().rstrip()
    print(homepage[nowpage])