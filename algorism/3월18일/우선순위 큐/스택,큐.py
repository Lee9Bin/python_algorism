""" 스택 구현하기 파이썬에서는 리스트를 이용해서 스택을 구현한다. 
스택은 선입후출
"""
stack = list()
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
# stack=[1,2,3,4]
stack.pop()
# stack=[1,2,3]
stack.pop()
# stack=[1,2]
stack.pop()
# stack=[1]
print(stack)

""" 큐는 리스트로도 구현이 가능하지만 효율적이지 않다 선입선출
따라서 collection deque를 사용 또는 queue모듈의 Queue클래스 사용
"""
from collections import deque
deque1 = deque()

deque1.append(1)
# deque1 = [1]
deque1.append(2)
# deque1 = [1,2]
deque1.appendleft(3) #appendleft를 사용하면 왼쪽에 넣을수있음
# deque1 = [3,1,2]

deque1.pop() # 맨뒤에가 빠지고
deque1.popleft() # 맨앞에가 빠지고

print(deque1)

from queue import Queue
que = Queue()
que.put(3)
que.put(2)
que.put(1)
print(que.get())