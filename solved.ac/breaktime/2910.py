import sys
n, c = map(int, sys.stdin.readline().split());
nums = list(map(int ,sys.stdin.readline().split()))
dic = {}

for i in nums:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

subDic = sorted(dic.items(), key= lambda x:x[1], reverse=True)
for i in subDic:
    for j in range(i[1]):
        print(i[0],end=" ")