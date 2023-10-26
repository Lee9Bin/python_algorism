t = int(input())

for tc in range(1,t+1):
    n = int(input())
    ans = 1e9
    cnt = 0
    stoneList = list(map(int,input().split()))

    for nowdist in stoneList:
        if abs(nowdist) < ans:
            ans = abs(nowdist)

    # 제일 가까운 값 구했어
    for nowdist in stoneList:
        if ans == abs(nowdist):
            cnt +=1

    print(f"#{tc} {ans} {cnt}")