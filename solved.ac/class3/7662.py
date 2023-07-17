import sys
import heapq
T = int(sys.stdin.readline())
for i in range(T):
    K = int(sys.stdin.readline())
    maxhq = []
    minhq = []
    maxdic = {}
    mindic = {}
    for j in range(K):
        commend = list(map(str,sys.stdin.readline().split()))
        if commend[0] == "I":
            if int(commend[1]) not in mindic and -int(commend[1]) not in maxdic:
                maxdic[-int(commend[1])] = 1
                mindic[int(commend[1])] = 1
            elif int(commend[1]) in mindic and -int(commend[1]) in maxdic:
                maxdic[-int(commend[1])] += 1
                mindic[int(commend[1])] += 1
            heapq.heappush(maxhq,-int(commend[1]))
            heapq.heappush(minhq,int(commend[1]))
        else:
            if commend[1] == "-1":
                while minhq and maxdic[-minhq[0]] == 0: 
                    heapq.heappop(minhq)
                if minhq:
                    mindic[heapq.heappop(minhq)] -= 1
            elif commend[1] == "1":
                while maxhq and mindic[-maxhq[0]] == 0: 
                    heapq.heappop(maxhq)
                if maxhq:
                    maxdic[heapq.heappop(maxhq)] -= 1

    while maxhq and mindic[-maxhq[0]] == 0: 
        heapq.heappop(maxhq)      
    while minhq and maxdic[-minhq[0]] == 0: 
        heapq.heappop(minhq)              
    if not maxhq or not minhq:
        print("EMPTY")
    else:
        print(-maxhq[0], minhq[0])
