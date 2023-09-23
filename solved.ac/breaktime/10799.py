import sys
st = (sys.stdin.readline().rstrip())
st = st.replace("()","*")
stack = []
ans = 0
for i in st:
    if i == "*":
        ans += len(stack)
        
    else:
        if i == ")":
            stack.pop()
            ans += 1
        else:
            stack.append(i)
print(ans)