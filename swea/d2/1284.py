t = int(input())

for tc in range(t):
    P, Q, R, S, W = map(int,input().split())
    aCompany = P*W
    
    if (W <= R):
        bCompany = Q
    else:
        bCompany = Q + (W-R)*S
    
    print(f"#{tc+1} {min(aCompany,bCompany)}")