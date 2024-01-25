import sys
import datetime
toDay = list(map(int ,sys.stdin.readline().split()))
dDay = list(map(int ,sys.stdin.readline().split()))

start = datetime.date(toDay[0], toDay[1], toDay[2])
finish = datetime.date(dDay[0], dDay[1], dDay[2])

ans = str(finish-start).split(" ")[0]

if int(ans) >= 365243:
    print("gg")
else:
    print(f"D-{ans}")