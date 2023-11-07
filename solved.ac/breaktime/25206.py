import sys
dic = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0,"C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

grade = []
for i in range(20):
    grade.append(list(map(str,sys.stdin.readline().split())))
totalp = 0
total = 0
for i in range(20):
    if grade[i][2] == "P":
        continue
    point = float(grade[i][1])
    nowgrade = grade[i][2]
    totalp += point * dic[nowgrade]
    total += point
print(totalp/total)