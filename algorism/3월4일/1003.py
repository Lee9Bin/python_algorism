# 문제가 원하는 것, 문제설명
# 문제에 주어진 피보나치 수열에 의해 1과 0이 
# 몇번 호출되는지 구하는 문제
# 어떻게 풀려고 하였는지 => 플로우차트
# n이 0과 1을 저장하여서 dp에 저장한 뒤 점화식 사용하기
# 코드 설명
def fibonacci(n):
    for i in range(2,n+1):
        dp0[i] = dp0[i-1] + dp0[i-2]
        dp1[i] = dp1[i-1] + dp1[i-2]
    return print(dp0[n],dp1[n])

T = int(input())
alist = list()
#dp0과 dp1로 나눈 이유는 0의 호출 횟수와 1의 호출 횟수
dp0 = [0]*41
dp0[0] = 1    # n이 0일때 값 저장
dp1 = [0]*41 # n이 1일때 값 저장
dp1[1] = 1
for i in range(T):
    a = int(input())
    alist.append(a)
for i in alist:
    fibonacci(i)
#dp0 1 0 1 1...
#dp1 0 1 1 2...