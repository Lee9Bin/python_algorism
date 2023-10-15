import sys
e, s, m = map(int,sys.stdin.readline().split())
left, mid, end = 0, 0, 0
year = 0

while True:
    if e == left and s == mid and m == end:
        break
    left += 1
    mid += 1
    end += 1
    year += 1
    
    if left == 16:
        left = 1
    if mid == 29:
        mid = 1
    if end == 20:
        end = 1
print(year)