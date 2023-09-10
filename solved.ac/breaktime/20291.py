import sys
n = int(sys.stdin.readline())
dic = {}

for i in range(n):
    file = list(map(str,sys.stdin.readline().rstrip().split(".")))
    if file[1] not in dic:
        dic[file[1]] = 1
    else:
        dic[file[1]] +=1

result = []
for a in (dic.keys()):
    result.append((a,dic[a]))
result.sort() 

for i in result:
    print(*i)