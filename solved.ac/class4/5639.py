import sys
sys.setrecursionlimit(10**6)
node = []

while True:
    try:
        node.append(int(sys.stdin.readline()))
    except:
        break
tree = []
def post(start, end):
    if start > end-1:
        return
    mid = start +1 
    for i in range(start+1 , end):
        if node[start] < node[i]:
            mid = i
            break
    post(start+1,mid)
    post(mid,end)
    print(node[start])
post(0,len(node))