t = int(input())

for tc in range(t):
    sen = input()
    for i in range(1,30):
        nowsen = sen[:i]
        flag = True
        for j in range(0,30-(30%i),i):
            if nowsen != sen[j:j+i]:
                break
            if j == (30-(30%i) - i):
                flag = False
        if flag == False:
            print(f"#{tc+1} {len(nowsen)}")
            break