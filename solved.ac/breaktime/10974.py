import sys
n=int(sys.stdin.readline())
result= []
def back():
    if len(result) == n:
        return print(*result)
    for i in range(1,n+1):
        if visited[i]==False:
            result.append(i)
            visited[i]=True
            back() 
            visited[i]=False
            result.pop()

visited =[False]*(n+1)
back()