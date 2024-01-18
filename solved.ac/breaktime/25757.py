import sys
dic = {"Y":1, "F":2, "O":3}
n, kind = map(str, sys.stdin.readline().split())

apply = {}

for i in range(int(n)):
    nowName = sys.stdin.readline().rstrip()
    if nowName not in apply:
        apply[nowName] = 1
    
print(len(apply)//dic[kind])