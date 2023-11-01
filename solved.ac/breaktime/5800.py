import sys
k = int(sys.stdin.readline())
for i in range(k):
    classes = list(map(int,sys.stdin.readline().split()))
    print(f"Class {i+1}")
    maxValue = max(classes[1:])
    minValue = min(classes[1:])

    subClass = list(sorted(classes[1:]))
    gap = 0
    for i in range(classes[0]-1):
        if gap < subClass[i+1]-subClass[i]:
            gap = subClass[i+1]-subClass[i]
    
    print(f"Max {maxValue}, Min {minValue}, Largest gap {gap}")