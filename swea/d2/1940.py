t = int(input())

for tc in range(1,t+1):
    n = int(input())
    ans = 0
    speed = 0
    for i in range(n):
        command = list(map(int,input().split()))
        if len(command) != 1:
            if command[0] == 1:
                speed += command[1]
                ans += speed
            else:
                speed -= command[1]
                if speed < 0:
                    speed = 0
                ans += speed
        else:
            ans += speed
    print(f"#{tc} {ans}")