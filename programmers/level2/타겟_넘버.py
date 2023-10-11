# 문제설명: 주어진 숫자 배열에 적절히 더하고 빼서 target값이 나오는 경우의 수를 구하기
#         즉, 배열의 숫자들을 모두 더 할건데 적절히(모두 확인해야겠네) 부호를 바꿔가면서!
# 생각한 풀이
# 첫번째: 숫자들을 합할 때 + - 가 붙는 모두의 경우를 생각해야한다.
#       dfs가 떠올랐다. why? 그림을 그려보면 알수 있다.
#                 0
#     numbers[0]    -numbers[0]
cnt=0
def solution(numbers, target):
    answer = 0
    dfs(0, target, 0, 0, numbers)
    answer=cnt
    return answer
def dfs(index,target,total,depth,arr):
    global cnt
    if depth == len(arr):
        if total == target:
            cnt +=1
        return
    dfs(index+1, target, total+arr[index],depth+1,arr)
    dfs(index+1, target, total-arr[index],depth+1,arr)