prim = [2]
for i in range(3,1000):
        for j in range(2,i):
            if i % j == 0:
                break
            if j == i-1:
                prim.append(i)
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    cnt = 0
    for i in range(len(prim)):
        result = prim[i]
        for j in range(i,len(prim)):
            result += prim[j]
            for k in range(j,len(prim)):
                result += prim[k]
                if result == n:
                    cnt +=1
                result -=prim[k]
            result -= prim[j]
    print(f"#{test_case} {cnt}")