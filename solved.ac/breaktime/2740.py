import sys
n,m = map(int,sys.stdin.readline().split())
A = []
for i in range(n):
    A.append((list(map(int,sys.stdin.readline().split()))))


m,k = map(int,sys.stdin.readline().split())
B = []
for i in range(m):
    B.append((list(map(int,sys.stdin.readline().split()))))

result = [[0 for i in range(k)] for i in range(n)]

for i in range(n):
    for j in range(k):
        for x in range(m):
            result[i][j] += (A[i][x] * B[x][j])


for i in result:
    print(*i)