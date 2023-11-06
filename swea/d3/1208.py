for i in range(10):
    n = int(input())
    box = list(map(int,input().split()))
    
    # 계속 정렬을 해주는게 나으려나 ..
    
    for k in range(n):
        box.sort()
        if abs(box[0] - box[-1]) <= 1:
            break
        box[0] += 1
        box[-1] -= 1
    box.sort()
    print(f"#{i+1} {box[-1]-box[0]}")