import sys

leapYear = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
commonYear = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

start = list(map(int ,sys.stdin.readline().split()))
end = list(map(int ,sys.stdin.readline().split()))

ans = 0
for year in range(start[0], end[0]+1):
    target = commonYear
    if(year % 4 == 0 and year % 100 !=0 or year % 400 == 0):
        target = leapYear
    
    if year == start[0]:
        ans += target[start[1]]-start[2]
        for i in range(start[1]+1, 13):
            ans += target[i]
    elif year == end[0]:
        for i in range(1,end[1]):
            ans += target[i]
        ans += end[2]
    else:
        ans += sum(target[i] for i in range(1, 13))

gg = 0
for year in range(start[0], start[0]+1001):
    target = commonYear
    if(year % 4 == 0 and year % 100 !=0 or year % 400 == 0):
        target = leapYear
    
    if year == start[0]:
        gg += target[start[1]]-start[2]
        for i in range(start[1]+1, 13):
            gg += target[i]
    elif year == start[0]+1000:
        for i in range(1,start[1]):
            gg += target[i]
        gg += start[2]
    else:
        gg += sum(target[i] for i in range(1, 13))
if ans >= gg:
    print("gg")
else:
    print(f"D-{ans}")
