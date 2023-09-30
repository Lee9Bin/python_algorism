import sys
senten = sys.stdin.readline().rstrip()
dic = {}

for i in range(len(senten)):
    now = senten[i]
    if now in dic:
        dic[now] += 1
    else:
        dic[now] = 1
    for j in range(i+1,len(senten)):
        now += senten[j]
        if now in dic:
            dic[now] += 1
        else:
            dic[now] = 1
print(len(dic))
