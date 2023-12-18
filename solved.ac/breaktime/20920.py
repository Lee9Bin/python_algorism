import sys
n,m = map(int, sys.stdin.readline().split())

dic = {}

for i in range(n):
    senten = sys.stdin.readline().rstrip()
    if len(senten) >= m:
        if senten not in dic:
            dic[senten] = 1
        else:
            dic[senten] += 1
            

result = sorted(dic.items(), key=lambda x:(-x[1],-len(x[0]),x[0]))

for i in result:
    print(i[0])