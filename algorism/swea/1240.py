# 3 33
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int,input().split())
    code = []
    for i in range(n):
        a = input()
        for i in range(m-1,-1,-1):
            if a[i] == '1':
                code = a[:i+1]
                break
    result = []
    for i in range(len(code),-1,-7):
        if code[i-1] == '1':
            result.append(code[i-7:i])
        else:
            break
    result.reverse()
    numlist = ['0001101','0011001','0010011','0111101','0100011',
               '0110001','0101111','0111011','0110111','0001011']
    ans= []
    for i in result:
        ans.append(numlist.index(i))
    hab = 0
    for i in range(len(ans)):
        if i % 2 ==0:
            hab += 3*ans[i]
        else:
            hab += ans[i]
    if hab % 10 != 0:
        hab = 0
    else:
        hab = sum(ans)
    print(f"#{test_case} {hab}")
# 한줄씩 입력바아서 어떻게 7개씩 잘라서 넣을거야 ?
# str로 받으면 전체 길이 저장 가능 이게 맞아