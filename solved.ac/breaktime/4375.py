import sys
while True:
    now = 0
    cnt = 0
    try:
        n = int(sys.stdin.readline())
    except:
        break
    while True:
        now = now * 10 + 1
        cnt += 1
        if now % n == 0:
            print(cnt)
            break