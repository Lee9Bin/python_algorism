import sys
def stop(x):
    if x == 0:
        return True
while True:
    M = int(sys.stdin.readline())
    if stop(M) == True:
        break
    sen = sys.stdin.readline().strip()
    check = list()
    left,right = 0 , 0
    cnt, size = 0 , 0
    
    while left <= right:
        if cnt < M or (cnt == M and sen[right] in check):
            if sen[right] not in check:
                cnt +=1
            check.append(sen[right])
            right += 1
        else:
            if check.count(check[0]) == 1:
                cnt -=1
            check.remove(check[0])
            left +=1
        
        size = max(right-left,size)
        if right == len(sen)-1:
            break
    print(size)