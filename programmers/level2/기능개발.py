# 문제설명: 각 기능마다 작업의 진도가 주어지고 하루 개발 속도가 주어진다.
#         이때 뒤에 있는 기능이 먼저 개발 완료 될 수 있지만 앞에 있는 기능이 완료돼서 배포 되지 않으면
#         배포 되지 않는다 -> 오호라 선업선출의 규칙이 이루어져야겠다.
# 하루하루 지나면서 맨 앞에 있는 기능이 100퍼를 넘었는지 체크한다.
# 넘었다면 바로 뒤에 있는 기능 확인 -> 반복!
from collections import deque
def solution(progresses, speeds):
    answer = []
    ans = len(progresses)
    progresses = deque(progresses)
    speeds = deque(speeds)
    while True:
        cnt = 0
        if sum(answer) == ans:
            break
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            while progresses:
                if progresses[0] < 100:
                    break
                else:
                    cnt += 1
                    progresses.popleft()
                    speeds.popleft()
        if cnt >0:
            answer.append(cnt)
    return answer