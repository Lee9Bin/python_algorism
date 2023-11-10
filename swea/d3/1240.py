t = int(input())
dic = {"0001101":0, "0011001":1, "0010011":2, "0111101":3,
       "0100011":4, "0110001":5, "0101111":6, "0111011":7,
       "0110111":8, "0001011":9}
for tc in range(t):
    n, m = map(int,input().split())
    graph = []
    
    for i in range(n):
        graph.append(list(map(str,input())))
    # print(graph)
    ans = []
    for i in range(n):
        for j in range(m-55):
            result = []
            nowpassword = ''.join(graph[i][j:j+56])
            for k in range(8):
                if nowpassword[k*7:k*7+7] in dic:
                    result.append(dic[nowpassword[k*7:k*7+7]])
            if len(result) == 8:
                ans = result
                break
    
    oddNumber = 0
    evenNumber = 0
    for i in range(8):
        if i % 2 != 0:
            evenNumber += ans[i]
        else:
            oddNumber += ans[i]
            
    if ((oddNumber*3)+evenNumber)%10 == 0:
        print(f"#{tc+1} {sum(ans)}")
    else:
        print(f"#{tc+1} {0}")