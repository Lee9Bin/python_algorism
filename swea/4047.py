# 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s = []
    d = []
    h = []
    c = []
    ans = 0
    card = list(map(str, input()))
    for i in range(0,len(card),3):
        if card[i] == 'S':
            if int(card[i+1]+card[i+2]) not in s:
                s.append(int(card[i+1]+card[i+2]))
            else:
                ans = 'ERROR'
                break
        elif card[i]== 'D':
            if int(card[i+1]+card[i+2]) not in d:
                d.append(int(card[i+1]+card[i+2]))
            else:
                ans = 'ERROR'
                break
        elif card[i]== 'H':
            if int(card[i+1]+card[i+2]) not in h:
                h.append(int(card[i+1]+card[i+2]))
            else:
                ans = 'ERROR'
                break
        else:
            if int(card[i+1]+card[i+2]) not in c:
                c.append(int(card[i+1]+card[i+2]))
            else:
                ans = 'ERROR'
                break
    if ans == 'ERROR':
        print(f"#{test_case} {ans}")
    else:
        print(f"#{test_case} {13-len(s)} {13-len(d)} {13-len(h)} {13-len(c)}")
    # print(f"#{test_case} {0}")