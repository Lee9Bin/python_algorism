# 3 45
T = int(input())
nlist= []
for i in range(2,int(1000000000**(0.5))):
    for j in range(2,i+1):
        if j == i:
            nlist.append(i)
        if i % j == 0:
            break
result = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    ans = 1
    # 입력받은 숫자를 소수로만 나눠 왜? 다른 값들은 다 2로 나누어지거든
    for i in nlist:
        cnt = 0
        # 만약 n이 리스트에 담긴 값을 나누어떨어지면 더이상 나누어 지지 않을때까지 나눈다음에 다음 소수로
        while n % i == 0:
            n = n//i
            cnt +=1
        if cnt % 2 != 0:
            ans = ans *i
        if n == 1 or i > n:
            break
    result.append(f"#{test_case} {ans}")
for i in result:
    print(i)
#  12 6 3 
# 먼가 숫자범위를 돌면서 i로 n을 나눠봐 그러고 나서 남은 몫이 어떤수의 제곱이면 ok
#  1000 10->100 \
#  루트 표현 a**(1/2)