n = int(input())
result = []
check = ['3','6','9']
for i in range(1,n+1):
    sub = []
    for j in str(i):
        if j in check:
            sub.append('-')
    if len(sub) == 0:
        result.append(i)
    else:
        result.append(''.join(sub))
print(*result)