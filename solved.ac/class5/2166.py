# 처음에는 각 좌표의 중점을 찾아서 각 변의 길이를 구해서 삼각형으로 쪼개서 계산하려 했다.
# 하지만 쉽지않았다.
# 신발끈 공식 -> 가능한 이유 다각형을 이루는 순서대로 값이 들어옴
import sys
n = int(sys.stdin.readline())
x = []
y = []

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    x.append(a)
    y.append(b)

x.reverse()
y.reverse()
x.append(x[0])
y.append(y[0])
upTotal = 0
downTotal =0
for i in range(n):
    upTotal += x[i] * y[i+1]
    downTotal += y[i] * x[i+1]
result = round(abs(upTotal-downTotal)/2,1)
print(result)