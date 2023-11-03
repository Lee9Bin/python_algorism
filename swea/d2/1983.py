t = int(input())
grade = ["A+", "A0", "A-","B+", "B0", "B-","C+", "C0", "C-","D0"]

for tc in range(1,t+1):
    n, k =map(int,input().split())
    student = []
    
    for i in range(n):
        mid, end, homework = map(int,input().split())
        student.append(mid*0.35 + end*0.45 + homework*0.2)
    findScore = student[k-1]
    
    student.sort(reverse=True)

    change = n//10
    print(f"#{tc} {grade[student.index(findScore)//change]}")