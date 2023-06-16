import sys

n=int(sys.stdin.readline())
numlist=[]

for i in range(n):
    numlist.append(int(sys.stdin.readline()))

numlist.sort()

print(round(sum(numlist)/n))
print(numlist[n//2])

#최빈값
dic=dict()
for i in numlist:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
        
mx=max(dic.values())
mx_dic=[]

for i in dic:
    if mx==dic[i]:
        mx_dic.append(i)

if len(mx_dic)>1:
    print(mx_dic[1])
else:
    print(mx_dic[0])
    
print(numlist[-1]-numlist[0])