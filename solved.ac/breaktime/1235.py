import sys
n = int(sys.stdin.readline())

students = []

for i in range(n):
    student = sys.stdin.readline().rstrip()
    students.append(student)

ans = 0

for i in range(len(students[0])-1, -1,-1):
    result = []
    for j in students:
        if j[i:] in result:
            break
        else:
            result.append(j[i:])

    if len(result) == n:
        ans = len(result[0])
        break

print(ans)