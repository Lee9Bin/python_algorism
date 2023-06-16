# 다시 학습해보기
import sys
import math
m, n = map(int, sys.stdin.readline().split())
array = [True for i in range(n + 1)] 
# 에라토스테네스의 체 알고리즘 
for i in range(2, int(math.sqrt(n)) + 1): 
    if array[i] == True: 
        j = 2 
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(m, n + 1):
    if i ==1 :
        continue
    if array[i]:
        print(i)