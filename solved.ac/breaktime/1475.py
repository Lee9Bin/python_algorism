import sys
n=sys.stdin.readline().rstrip()
dic = {}
for i in n:
    if i == '9' or i=='6':
        i = 't'
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
ans = 0
for key in dic:
    if key == 't':
        if dic[key] % 2 != 0:
            if ans < dic[key]//2 + 1:
                ans = dic[key]//2 + 1
        else:
            if ans < dic[key]//2 :
                ans = dic[key]//2
    else:
        if ans < dic[key]:
            ans = dic[key]
print(ans)