import sys
t  = int(sys.stdin.readline())
for _ in range(t):
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().split())
    
    dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    
    # 두원의 좌표가 같고 반지름이 같다면 두원이 겹쳐지므로 무한개
    if dis == 0 and r1 == r2:
        print(-1)
    
    # 두 중심좌표의 거리가 반지름의 합과 같다면 외접 , 두 중심좌표의 거리가 두 반지름의 거리의 차이만큼이면 내접
    elif dis == r1+r2 or dis == abs(r1-r2):
        print(1)
    
    # 반지름의 합이 거리보다 크면 2점 ... 쭉 가다가 거리가 두 반지름의 차이보다 커지기전까지
    elif r1+r2 > dis and dis > abs(r1-r2):
        print(2)
    
    else:
        print(0)