t = int(input())

for tc in range(1,t+1):
    testNumber = int(input())
    score = list(map(int,input().split()))
    checkList = set(score)
    
    maxScore = 0
    result = []
    for i in checkList:
        result.append((i,score.count(i)))
    
    result.sort(key=lambda x:(x[1],x[0]),reverse=True)

    print(f"#{testNumber} {result[0][0]}")