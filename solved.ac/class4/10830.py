import sys
n, b = map(int,sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

def multy(a,b):
    sub = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
            for j in range(n):
                for k in range(n):
                    sub[i][j] += (a[i][k] * b[k][j])%1000
    return sub
    
def div(nowa,nowb):
    if nowb == 1:
        return nowa
    temp = div(nowa,nowb//2)
    if nowb % 2 == 0:
        return multy(temp,temp)
    else:
        return multy(multy(temp,temp),nowa)
result = div(graph,b)

# print(result)
for i in result:
    for j in i:
        print(j%1000,end=' ')
    print()