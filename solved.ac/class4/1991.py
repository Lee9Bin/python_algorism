import sys
n = int(sys.stdin.readline())
graph = {}

for i in range(n):
    root, left, right = map(str,sys.stdin.readline().split())
    graph[root] = [left,right]

def pre(root):
    if root != '.':
        print(root, end='')
        pre(graph[root][0])
        pre(graph[root][1])
        
def sen(root):
    if root != '.':
        sen(graph[root][0])
        print(root, end='')
        sen(graph[root][1])

def bef(root):
    if root != '.':
        bef(graph[root][0])
        bef(graph[root][1])
        print(root, end='')
        
pre("A")
print()
sen("A")
print()
bef("A")