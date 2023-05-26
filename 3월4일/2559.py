# 문제가 원하는 것, 문제설명
# N개의 수가 있는 수열에서 연속된 K만큼의 값들중 최대값

# 어떻게 풀려고 하였는지 => 플로우차트
# 배열에 담긴 값중 제일 큰놈을 기준으로 이 값을 포함하는 ... 안되지
# 도저히 모르겠어서 알고리즘 분류에 슬라이딩 윈도우라는 키워드 검색해서 풀이
# 리스트 슬라이싱으로 하면 안되는건가 ..?
# 범위에서만 확인

# 코드 설명
N, K = map(int,input().split())
temp = list(map(int, input().split()))
result = list()
st = 0        # 1
end = st + K  # 3
result.append(sum(temp[st:end]))
while end <= N-1:
    result.append(result[-1]-temp[st]+temp[end])
    st += 1
    end += 1
print(max(result))