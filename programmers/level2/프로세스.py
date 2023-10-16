# 문제설명: 실행 대기 큐에 대기중인 프로세스가 있는데 우선순위가 높은 것부터 나와야한다.
#           맨앞에 있는 프로세스를 꺼냈을 때 남은 프로세스중 현재 우선순위가 높은것 이 있으면 맨뒤로 넣기
#           없다면 뽑기 -> 큐에 동작과정을 활용한 구현문제라고 판단.
# 문제풀이
# location이라는 매개변수는 배열내의 프로세스 위치를 뜻하는데 몇번째로 나오는지 구하는거다.
# 단순히 큐에 넣고 빼서 값을 구하기는 어렵다
# 그래서 큐에 프로세스를 넣을때 원래의 위치(인덱스)를 같이 넣는다.
# 큐에서 뽑히는 순간 저장해 놓은 순서를 result배열에 저장한다. 어떻게? 큐에 같이 넣은 인덱스 위치에
from collections import deque
def solution(priorities, location):
    answer = 0
    result = [0]*(len(priorities))
    que = deque()
    for i in range(len(priorities)):
        que.append((priorities[i],i))
    cnt = 1
    while que:
        nowv,noww = que.popleft()
        flag = True
        for i in que:
            if nowv < i[0]:
                que.append((nowv,noww))
                flag = False
                break
        if flag == True:
            result[noww] = cnt
            cnt +=1
    answer = result[location]
    return answer