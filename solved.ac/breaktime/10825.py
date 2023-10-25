import sys
n = int(sys.stdin.readline())
students = []

for i in range(n):
    name, kr, en, mt = map(str,sys.stdin.readline().split())
    students.append([name,int(kr),int(en),int(mt)])
students.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in students:
    print(i[0])