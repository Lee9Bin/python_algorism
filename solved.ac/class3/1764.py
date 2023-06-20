import sys
n, m = map(int,sys.stdin.readline().split())

dic= {}
for i in range(n+m):
    human = sys.stdin.readline().rstrip()
    if human not in dic:
        dic[human] = 1
    else:
        dic[human] += 1

result = []
ans = 0
for i in dic:
    cnt = dic.get(i)
    if cnt >=2:
        ans +=1
        result.append(i)
print(ans)
result.sort()
for i in result:
    print(i)