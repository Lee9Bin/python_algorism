T = int(input())
for tc in range(1, T+1):
    # N: 사람수, M초의 시간을 들이면 K개의 붕어 만들수있음
    N, M, K = map(int, input().split())
    human= list(map(int, input().split()))
    human.sort()
    
    ans = "Possible"
    for i in range(1,N+1):
        cnt = (human[i-1]//M) * K - (i)
        if cnt < 0:
            ans = "Impossible"
            break
    print("#{} {}".format(tc, ans))
    