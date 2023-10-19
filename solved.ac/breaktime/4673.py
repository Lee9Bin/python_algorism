visited = [False] * (10001)
def self(n):
    if n > 10000:
        return
    visited[n] = True
    
    newn = n
    for i in str(n):
        newn += int(i)
    self(newn)

for i in range(1,10001):
    if visited[i] == False:
        print(i)
        self(i)
    