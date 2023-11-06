t = int(input())

def back(point, cal, start):
    global ans
    ans = max(ans, point)
    # print(point, cal)
    for i in range(start,n):
        if cal + foodList[i][1] <= l:
            back(point + foodList[i][0],cal+foodList[i][1], i + 1)
            
for tc in range(1,t+1):
    n, l = map(int,input().split())
    foodList = []
    
    for i in range(n):
        foodList.append(list(map(int,input().split())))
    
    foodList.sort(key=lambda x:x[1]) 
    
    ans = 0
    back(0,0,0)
    print(f"#{tc} {ans}")