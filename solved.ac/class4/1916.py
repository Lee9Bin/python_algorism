# import sys
# import heapq
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

# bus = [[] for i in range(n+1)]

# for i in range(m):
#     a,b,v = map(int,sys.stdin.readline().split())
#     bus[a].append((v,b))
# start, end = map(int,sys.stdin.readline().split())
# dis = [1e9] * (n+1)

# def dik(start):
#     hq = []
#     heapq.heappush(hq,(0,start))
#     dis[start] = 0
#     while hq:
#         dist, nown = heapq.heappop(hq)
        
#         if dis[nown] < dist:
#             continue    
        
#         for i in bus[nown]:
#             nowdist = i[0] + dist
#             if nowdist < dis[i[1]]:
#                 dis[i[1]]  = nowdist
#                 heapq.heappush(hq,(nowdist,i[1]))
                
# dik(start)
# print(dis[end])
import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

bus = [[1e9 for i in range(n+1)] for i in range(n+1)]

for i in range(m):
    a,b,v = map(int,sys.stdin.readline().split())
    if bus[a][b] > v:
        bus[a][b] = v
start, end = map(int,sys.stdin.readline().split())
dis = [1e9] * (n+1)

def dik(start):
    hq = []
    heapq.heappush(hq,(0,start))
    dis[start] = 0
    while hq:
        dist, nown = heapq.heappop(hq)
        
        if dis[nown] < dist:
            continue    
        
        for i in range(1,n+1):
            if bus[nown][i] != 1e9:
                nowdist = bus[nown][i] + dist
                if nowdist < dis[i]:
                    dis[i]  = nowdist
                    heapq.heappush(hq,(nowdist,i))
dik(start)
print(dis[end])