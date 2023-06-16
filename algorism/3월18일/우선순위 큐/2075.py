# 문제가 원하는 것, 문제설명
# N을 입력해서 N*N 행렬을 만드는데 모든 수는 
# 자신의 한칸 위에 있는 수보다 크다는 규칙을 가지고 생성

# 어떻게 풀려고 하였는지 => 플로우차트
# 처음에는 입력받는 값 모두 우선순위 큐에 저장해서 5번째로 큰값을 찾으려했다
# ---> 그랬더니 메모리 초과 발생

# 그래서 우선순위큐의 사이즈를 정하고 코드를 짜봤다.
# 코드 설명

import sys
from queue import PriorityQueue
N = int(sys.stdin.readline())
que = PriorityQueue(maxsize=N) # N번째 숫자를 구하는것이기에 사이즈를 N으로 제한

for i in range(N):
    # N 입력하고 다음 줄에 입력할때 큐는 무조건 비어 있기에 입력받는 값들 큐에 put
    if que.empty() == True: 
        quelist = list(map(int, sys.stdin.readline().split()))
        for j in quelist:
            que.put(j)

    else:
        quelist = list(map(int, sys.stdin.readline().split()))
        quelist.sort(reverse=True) # 그런 다음에 quelist에 담은뒤 오름차순으로 정렬 시켜준다
                                   # 정렬 시킨 이유는 else가 실행 되면 break 걸기위해
        for j in quelist: #오름차순으로 정렬된 원소를 가져와서 비교를 하는데
            parenum = que.get()
            if j > parenum: # 만약 원소가 que.get()으로 가져온 값보다 크면 원소를 추가
                que.put(j)
            else: #작거나 같다면 어차피 뒷순위이기에 넣지 않는다.
                que.put(parenum)
                break 
print(que.get())