import sys
n, m = map(int, sys.stdin.readline().split())
knowList = set(sys.stdin.readline().split()[1:])
parties = []

for i in range(m):
    parties.append(set(input().split()[1:]))

for i in range(m):
    for party in parties:
        if party & knowList:
            knowList = knowList.union(party)
        
print(knowList)
cnt = 0
for party in parties:
    if party & knowList:
        continue
    cnt += 1

print(cnt)