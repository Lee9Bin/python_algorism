import sys
n, m = map(int,sys.stdin.readline().split())
numlist = list(map(int,sys.stdin.readline().split()))
numlist.sort()  #비내림차순 만족해주기 위해 정렬

def back(start):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(start,n):
        result.append(numlist[i])
        back(i)
        result.pop()
    
result = []
back(0)