t = int(input())

for tc in range(1,t+1):
    firstTime, firstMinute, secondTime, secondMinute = map(int,input().split())
    
    totalTime = (firstTime + secondTime + (firstMinute+secondMinute)//60)
    while totalTime >= 12:
        totalTime -= 12
        
    totalMinute = (firstMinute+secondMinute)%60
    print(f"#{tc} {totalTime} {totalMinute}")