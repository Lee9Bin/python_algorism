t = int(input())
noSee = ["a", "e", "i", "o", "u"]
for tc in range(1,t+1):
    word = input()
    
    ans = ""
    
    for i in word:
        if i not in noSee:
            ans += i
            
    print(f"#{tc} {ans}")