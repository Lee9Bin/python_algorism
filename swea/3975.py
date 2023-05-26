# 만약 시간 초과 나면 입력값 저장해서 한번 해 출력
T = int(input())
ans = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a,b,c,d = map(int, input().split())
    alis = a/b
    bob = c/d
    
    if alis > bob:
        ans.append("ALICE")
    elif alis < bob:
        ans.append("BOB")
    else:
        ans.append("DRAW")
for i in range(T):
    print(f"#{i+1} {ans[i]}")

# 엘리스는 b전 a승
# ㅂ밥은 d전 c승