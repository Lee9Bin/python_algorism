import sys
n, m = map(int,sys.stdin.readline().split())
parent = [0] * n

for i in range(n):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
cycle = False
result = 0
for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    # if cycle == False and parent[a] == parent[b]:
    if cycle == False and find_parent(parent, a) == find_parent(parent, b):
        result = i+1
        cycle = True
    union_parent(parent,a,b)

if cycle == False:
    print(0)
else:
    print(result)