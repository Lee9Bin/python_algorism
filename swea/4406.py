# 
T = int(input())
word = ['a', 'e', 'i', 'o', 'u']
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    senten = input()
    ans = []
    for i in senten:
        if i not in word:
            ans.append(i)
    print(f"#{test_case} {''.join(ans)}")