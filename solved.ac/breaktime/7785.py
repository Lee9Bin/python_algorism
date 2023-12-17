import sys
n = int(sys.stdin.readline())

dic = {}

for i in range(n):
    name, state = map(str,sys.stdin.readline().split())
    if state == "enter":
        dic[name] = 1
    elif state =="leave":
        dic[name] = 0

result = []

for i in dic:
    if dic[i] == 1:
        result.append(i)

result.sort(reverse=True)

for i in result:
    print(i)