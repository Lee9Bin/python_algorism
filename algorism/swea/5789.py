# 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, q = map(int, input().split())
    box = [0]*n
    lr = []
    for i in range(q):
        l, r = map(int, input().split())
        lr.append((l,r))
    cnt =1
    for s,e in lr:
        for j in range(s-1,e):
            box[j] = cnt
        cnt +=1
    print(f"#{test_case}", end='')
    print(*box)
    
# 1부터 n번까지의 박스가 있다
