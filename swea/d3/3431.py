t = int(input())

for tc in range(1,t+1):
    l, m, x = map(int,input().split())
    if x <= l:
        print(f"#{tc} {l-x}")
    elif m <x:
        print(f"{tc} {-1}")
    else:
        print(f"{tc} {0}")