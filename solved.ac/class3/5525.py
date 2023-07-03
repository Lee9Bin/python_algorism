import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

start,end,cnt = 0,0,0

while end < m:
    # 슬라이싱을 쓰지만 범위를 늘리지않고 일정하게 유지하면서 시간단축
    # 패턴이 IOI, IOIOI...이므로 end:end+3이 IOI에 만족하면 end +=2
    if s[end:end+3] == "IOI":
        end += 2
        # 길이가 문제에서 제시한 길이와 동일하면 cnt를 +1해주고
        # start위치를 +2 시킨다 why? IOIOI라면 다음위치는 당연히 O일테고 다음 I로 가야하기 때문
        if end - start == 2*n:
            cnt +=1
            start +=2
    # 패턴에 맞지 않으면 그동안 확인한 부분들은 바로 뛰어넘어야하므로 start와 end위치를 end+1로 조정
    else:
        start = end+1
        end = end +1
print(cnt)