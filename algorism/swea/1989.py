# 3시 16분
# 그대로 읽는거 거꾸로 읽는거 같으면 회문


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    senten = list(input())
    subsent= list(reversed(senten))
    # for i in senten[::-1]:
    #     subsent.append(i)
    if senten == subsent:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")
