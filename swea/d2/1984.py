t = int(input())

for tc in range(1, 1+t):
    numlist = list(map(int,input().split()))
    
    numlist.sort()
    
    print(f"#{tc} {round(sum(numlist[1:9])/8)}")