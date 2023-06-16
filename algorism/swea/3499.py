# 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    senlist = list(map(str, input().split()))
    if n % 2 != 0:
        n += 1
    first = senlist[:n//2]
    secon = senlist[n//2:]
    cnt = 1
    for i in range(len(secon)):
        first.insert(i+cnt,secon[i])
        cnt +=1
    
    print(f"#{test_case}",end=' ')
    print(*first)