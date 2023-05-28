n = int(input())

def star(l):
    if l == 3:
        return ['***','* *','***']

    nowgraph = star(l//3)
    result = []
    
    for i in nowgraph:
        result.append(i*3)
    
    for i in nowgraph:
        result.append(i+' '*(l//3)+i)
    
    for i in nowgraph:
        result.append(i*3)
    
    return(result)
ans = star(n)    
for i in ans:
    print(i)