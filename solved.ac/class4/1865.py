import sys
# 다시 체크하기
def bellman(start, graph):
    dist = [1e9] * (n+1)
    dist[start] = 0
    
    for _ in range(n-1):
        for u in range(1, n+1):
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
    
    for u in range(1, n+1):
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                return True
    
    return False

tc = int(sys.stdin.readline())
for _ in range(tc):
    n, m, w = map(int, sys.stdin.readline().split())
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        graph[s].append((e, t))
        graph[e].append((s, t))
    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        graph[s].append((e, -t))
    
    if bellman(1, graph):
        print("YES")
    else:
        print("NO")