t = int(input())

for tc in range(1,1+t):
    n = int(input())
    result = [[1]]
    
    for i in range(1,n):
        addList = []
        for j in range(i+1):
            total = 0
            if j-1 >= 0 and j-1 <len(result[i-1]):
                total += result[i-1][j-1]
            
            if len(result[i-1]) > j:
                total += result[i-1][j]
                
            addList.append(total)
        result.append(addList)
    
    print(f"#{tc}")
    for i in result:
        print(*i)