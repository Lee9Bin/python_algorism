T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int,input().split())
    
    result = []
    
    for i in range(n):
        a,b,c = map(int,input().split())
        
        result.append(a*0.35+b*0.45+c*0.2)
    
    student = result[k-1]
    result.sort(reverse=True)
    grade= ['A+',
            'A0',
            'A-',
            'B+',
            'B0',
            'B-',
            'C+',
            'C0',
            'C-',
            'D0'
            ]
    v= 0
    cnt = 0
    for i in result:
        cnt += 1
        if i == student:
            print(f"#{test_case} {grade[v]}")
        if cnt % (n/10)==0:
            v+=1
        