""" 
제일 높은곳에 있는 상자를 제일 낮은곳에 있는곳으로 옮기는 작업을 덤프
"""

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n = int(input())
    box = list(map(int, input().split()))
    
    for i in range(n):
        box.sort(reverse=True)
        box[0] = box[0] - 1
        box[-1] = box[-1] +1
    box.sort(reverse=True)
    print(f"#{test_case} {box[0]-box[-1]}")