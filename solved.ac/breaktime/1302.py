import sys
import heapq
n = int(sys.stdin.readline())

strList = []

for i in range(n):
    strList.append(sys.stdin.readline().rstrip())

dic = {}

for i in strList:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

result = []
for i in dic:
    result.append((dic[i],i))
    
result.sort(key=lambda x:(-x[0],x[1]))
print(result[0][1])