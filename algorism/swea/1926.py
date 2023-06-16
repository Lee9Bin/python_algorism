# 5시 37분
# 숫자 1부터 차례대로 말하는데 3 6 9가 들어간 수는 말하지 않기
# 말하지 않는 대신 박수 박수스는 3 6 9 갯수 만큼

n = int(input())

result = list()
clap = ['3','6','9']

for i in range(1,n+1):
    i = str(i)
    cnt = 0
    for j in i:
        if j in clap:
            cnt +=1
    if cnt >0 :
        result.append('-'*cnt)
    else :
        result.append(i)

for i in result:
    print(i,end=' ')   