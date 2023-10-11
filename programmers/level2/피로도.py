# 문제설명: 각 던전의 최소 입장 피로도와 소모 피로도가 주어진다.
#         던전에 입장전 피로도가 주어진다.
#         이때 던전을 어떤 순서로 돌아야 가장 많이 돌수 있는지 구하기!
# 생각한 풀이
# 첫번째: 던전들을 어떤 순서에 따라 돌때 다음 던전으로 갈 수 있는지 없는지 피로도에 의해 결정된다.
#       -> 그렇다면 순서에 따라 도는 던전의 경우의수를 구하고 얼마나 던전을 지나왔는지 구하자
#          백트래킹!
ans=0
def solution(k, dungeons):
    visited =[False]*(len(dungeons))
    back(k,dungeons,0, visited)
    answer=ans
    return answer
def back(hp, dun,cnt,visited):
    global ans
    if ans<cnt:
        ans =cnt
    for i in range(len(dun)):
        if hp >= dun[i][0] and visited[i] ==False:
            visited[i]=True
            back(hp-dun[i][1],dun,cnt+1,visited)
            visited[i]=False
    return
        