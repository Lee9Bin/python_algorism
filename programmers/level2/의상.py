# 문제설명: 여러종류의 의상이 주어지고 각 의상들을 조합해 만들수 있는 경우의수 구하기
# 생각한 풀이
# 의상의 정보를 다 고대로 저장을 할 필요가 없다 -> 우리는 경우의 수만 알면 되기때문에 각 의상의 카테고리명만 알고 각 갯수만 구하자
# 해시 -> key value 형태로 저장하자. 해시는 검색에 유리하다.
# 따라서 각 의상의 카테코리 수를 구해 +1(아무것도 고르지 않았을때) 씩 해준뒤 모두 곱하고 -1을(적어도 의상하나는 입고 있어야한다.)한다.

def solution(clothes):
    answer = 0
    dic = {}
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]] = 1
        else:
            dic[i[1]] += 1
    
    total = 1
    for i in dic:
        total *= (dic[i]+1)
    answer = total -1
    return answer