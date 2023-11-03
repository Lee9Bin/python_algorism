t = int(input())

for tc in range(1,t+1):
    n = int(input())
    allString = ""
    length = 0
    for i in range(n):
        word = list(map(str,input().split()))
        allString += word[0]*int(word[1])
        length += int(word[1])
        
    print(f"#{tc}")
    for i in range(length//10+1):
        print(allString[i*10:i*10+9])