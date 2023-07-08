import sys
numlist = [0,1,2,3,4,5,6,7,8,9]
N = sys.stdin.readline().strip()
M = int(sys.stdin.readline())

# 망가진게 있는 경우에만 받아오기
if M > 0:
    broke = list(map(int, sys.stdin.readline().split()))
    for i in broke:
        numlist.remove(i)
        
# 현재 채널에서 + - 만해서 저장
result = abs(100-int(N))

def dfs():
    # 백트래킹을 통해 모든 경우의 수 계산
    global result
    if len(sublist) >0:
        if len(sublist) == len(N)-1 or len(sublist) == len(N) or len(sublist) == len(N)+1:
            nown = int(''.join(map(str,sublist)))
            if abs(nown-int(N)) + len(sublist) < result:
                result = abs(nown-int(N)) + len(sublist)
            if len(sublist) == len(N)+1:
                return
    for i in range(len(numlist)):
        sublist.append(numlist[i])
        dfs()
        sublist.pop()
        
sublist = []
if numlist:
    dfs()
print(result)