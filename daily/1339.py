import sys
n= int(sys.stdin.readline())
wordlist = []

dic = {}
for i in range(n):
    word = sys.stdin.readline().rstrip()
    length = len(word)
    
    for i in word:
        if i not in dic:
            dic[i] = 0
            dic[i] += 10**(length-1)
        else:
            dic[i] += 10**(length-1)
        length-=1
nlist = []
for i in dic:
    nlist.append(dic[i])
nlist.sort(reverse=True)
result = 0
n = 9
for i in nlist:
    result += n*i
    n -=1
print(result)



# 그리디
# 최대한을 만들고 싶어
# 그렇담 긴단어 기준으로 맨앞이 9가 오는게 좋겠다 틀린생각
 
# 파이썬 딕셔너리에 대해서 배움
# 딕셔너리란 사전형 데이터를 의미하며
# 딕셔너리는 중괄호!!!! -->  { }
# {key:value}
# 딕셔너리 값 다루기 
# 추가할거라면 dic{새로운키} = 값
# 수정을할거라면 dic{수정할키} = 새로운 값
# key 나 value 각각의 값을 가져오고 싶으면
# dic.key() ,   dic.value()
# sort 는 내부적으로 정렬되어 원본에 저장
# sorted는 정렬된 복사본을 생성한다
# 리스트.sort(key=lamda x:x[기준])