# 문제가 원하는 것, 문제설명
# 어떻게 풀려고 하였는지 => 플로우차트
#
import sys
from queue import PriorityQueue
N = int(sys.stdin.readline())
que = PriorityQueue() #큐 라는 변수명에 우선순위 큐를 부여
cnt = 0
for i in range(N):
    x = int(sys.stdin.readline())
    if i == 0:
        dasom = x
    # que.put()할때 제일 큰값을 가져오고 싶어서 -값으로 put
    else:
        que.put(-x)
        
if que.empty()==False: #큐에 원소가 하나라도 있으면 false
    while True:
        # -로 저장했으니
        maxnum = -(que.get())  #-7을 가져오고 7을 저장
        # get으로 가져오는 값이 다솜이보다 크면 다솜이 값을+1 해주고
        # 가져온 값은 -1해준뒤 put하면서 반복
        if dasom <= maxnum:
            dasom +=1
            maxnum -= 1 
            que.put(-maxnum)
            cnt +=1
        else:
            break   
    print(cnt)
else:
    print(0)