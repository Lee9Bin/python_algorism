import sys
n = int(sys.stdin.readline())
human = []

for i in range(n):
    human.append(list(map(int,sys.stdin.readline().split())))
    
ans = [0] * (n)

for i in range(n):
    nowkg,nowcm = human[i]
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        if nowkg<human[j][0] and nowcm < human[j][1]:
            cnt += 1
    ans[i] = cnt + 1
print(*ans)