""" 
n!이 있을때 n!안에 5의 갯수를 세면 된다
 """
M =int(input())
left = 1
right = 5*M
cnt = 0
result = list()
while left <= right:
    mid = (left + right) // 2 #mid값 설정
    
    temp = mid   #5의 개수를 세기 위한 변수 설정
    while temp >=5:
        temp //= 5
        cnt += temp
    
    if cnt < M:
        left = mid +1
        cnt =0
    else:
        right = mid - 1
        if cnt == M:
            result.append(mid)
        cnt = 0
if len(result) == 0:
    print(-1)
else:
    print(min(result))
