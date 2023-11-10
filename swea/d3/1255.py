from collections import deque

for i in range(10):
    n = int(input())
    
    numlist = deque(map(int,input().split()))
    
    # 앞에서 꺼내서 뒤로 보내야하기때문에 큐를 사용하는게 유리
    cnt = 1
    while True:
        if numlist[-1] == 0:
            break
        nowNum = numlist.popleft()
        nowNum -= cnt
        cnt += 1
        if nowNum < 0:
            nowNum = 0
        numlist.append(nowNum)
        if cnt == 6:
            cnt = 1
    print(f"#{n}",end=" ")
    for i in numlist:
        print(i,end=" ")
    print()
