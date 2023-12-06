import sys

n, kim, lim = map(int, sys.stdin.readline().split())
ans = 0
while kim != lim:
    
    kim -= kim//2
    lim -= lim//2
    ans +=1
print(ans)