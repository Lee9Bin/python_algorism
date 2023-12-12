import sys
strlist = []

for i in range(5):
    strlist.append(sys.stdin.readline().rstrip())

for i in range(15):
    for j in range(15):
        try:
            print(strlist[j][i],end="")
        except:
            continue
    
