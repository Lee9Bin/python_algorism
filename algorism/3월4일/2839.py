# 문제가 원하는 것, 문제설명
# N이 주어질 때 3킬로봉지와 5킬로 봉지를 사용해서 
# 최대한 적은 개수의 봉지를 사용하는 경우의 수 찾기

# 어떻게 풀려고 하였는지 => 플로우차트
# N이 주어졌을때 5와 3으로 N이 만들어질때 (5,3) (5,5,3,3)..일때
# 남은 값을 5나 3으로만 나눌때의 경우의수를 따져봤다

# 코드 설명
N = int(input())
result = list()
for i in range(0,(N//8)+1): #N을 8로 나누어서 몫까지의 경우의수
    a = N - 8*i
    if a % 5 == 0 and a % 3 == 0:
        result.append(i*2 + a//5)
    elif a % 5 == 0:
        result.append(i*2 + a//5)
    elif a % 3 == 0:
        result.append(i*2 + a//3)
if len(result) == 0: #위에의 경우가 하나도 담기지 않으면 5와 3으로 조합이 안돼
    print(-1)
else:
    print(min(result))