T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num , cnt = map(int, input().split())
    numlist = list()
    n = 0
    ans = 0
    visited = []
    for i in str(num):
        numlist.append(int(i))
    
    def DFS(n):
        global ans
        if n == cnt :
            ans = max(ans,int("".join(map(str,numlist))))
            return
        
        for i in range(0,len(numlist)-1):
            for j in range(i+1,len(numlist)):
                numlist[i],numlist[j] = numlist[j], numlist[i]
                nownum = int("".join(map(str,numlist)))+n
                if nownum not in visited:
                    visited.append(nownum)
                    DFS(n+1)
                numlist[i],numlist[j] = numlist[j], numlist[i]
                
            
    DFS(0)
    print(f"#{test_case} {ans}")

""" 1. 숫자와 횟수를 입력받는다
2. 숫자의 뒷부분부터 체크한다.
3. 가장큰수가 맨앞자리에 위치한게 아니면 무조건 바꿔

난 처음에 그리디로 판단했어 근데 이게 반례랑 과정에 확신이 드는 로직이 없다면
전체 탐색을 해보는것도 방법인데 시간초과 주의
"""