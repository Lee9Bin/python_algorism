import sys
n = int(sys.stdin.readline())
human = []
for i in range(n):
    human.append(list(map(str,sys.stdin.readline().split())))

human.sort(key=lambda x:(int(x[3]),int(x[2]),int(x[1])))
print(human[-1][0])
print(human[0][0])