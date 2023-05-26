# 스택 후입선출
# 큐 선입선출
from queue import PriorityQueue

que = PriorityQueue() #큐 라는 변수명에 우선순위 큐를 부여
# 기본적으로 우선순위 큐의 사이즈는 무한대 
# but PriorityQueue(maxsize=값 설정) 하면 최대사이즈 제한 할수 있음
que.put(1)
que.put(2)
que.put(4)
que.put(5)
que.put(3)
# 오름차순으로 get()해줌
print(que.get())
print(que.get())
print(que.get())
print(que.get())
print(que.get())
# 내림차순으로 하고싶으면 -붙여봐
que.put(-1)
que.put(-2)
que.put(-4)
que.put(-5)
que.put(-3)
print(-(que.get()))
print(-(que.get()))
print(-(que.get()))
print(-(que.get()))
print(-(que.get()))

# 우선순위를 부여하고 싶다
que.put((1,'1등')) #que.put(우선순위,값)
que.put((2,'2등'))
que.put((3,'3등'))
que.put((4,'4등'))
que.put((5,'5등'))
print(que.get()[1])
