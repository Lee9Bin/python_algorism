import sys

n = int(sys.stdin.readline())
human = []
for i in range(n):
    human.append(list(map(int, sys.stdin.readline().split())))

result = []
for i in range(n):
    kg, cm = human[i]
    cnt = 0
    for j in range(n):
        difkg, difcm = human[j]
        if kg < difkg and cm < difcm:
            cnt += 1
    result.append(cnt + 1)
print(*result)
