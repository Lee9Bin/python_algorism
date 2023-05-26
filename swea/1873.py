T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 그래프 정보 입력
    h,w = map(int,input().split())
    graph = []
    for i in range(h):
        graph.append(list(map(str,input())))
    # 무브리스트 입력
    n = int(input())
    movelist = list(map(str,input()))
    
    # 바라보는 방향 리스트 선언
    way = ['^','v','<','>']
    # 이동 정보 리스트 선언
    # 방향을 바꾸고 그곳이 평지면 이동
    move = ['U','D','L','R','S']
    # 땅정보 평지 벽돌 강철 물
    ground = ['.','*','#','-']
    
    # 현재위치 뽑아내자
    for i in range(h):
        for j in range(w):
            if graph[i][j] in way:
                nowx,nowy = i,j

    dx = [-1 ,1, 0, 0]
    dy = [0, 0, -1, 1]
    # 무브리스트 돌면서 해당 기능 수행
    for i in movelist:
        potanx, potany = nowx,nowy
        if i == 'S':
            potanx = potanx + dx[way.index(graph[nowx][nowy])]
            potany = potany + dy[way.index(graph[nowx][nowy])]
            if potanx < 0 or potany < 0 or potanx>h-1 or potany>w-1:
                continue
            if graph[potanx][potany] in ['.','-']:
                while True:
                    potanx = potanx + dx[way.index(graph[nowx][nowy])]
                    potany = potany + dy[way.index(graph[nowx][nowy])]
                    if potanx < 0 or potany < 0 or potanx>h-1 or potany>w-1:
                        break
                    if graph[potanx][potany] == '*':
                        graph[potanx][potany] = '.'
                        potanx,potany = nowx,nowy
                        break
                    elif graph[potanx][potany] == '#':
                        potanx,potany = nowx,nowy
                        break
            elif graph[potanx][potany] == '*':
                graph[potanx][potany] = '.'
                potanx,potany = nowx,nowy
            else:
                potanx,potany = nowx,nowy
        else:
            nextx = nowx + dx[move.index(i)]
            nexty = nowy + dy[move.index(i)]
            if nextx < 0 or nexty < 0 or nextx>h-1 or nexty>w-1:
                graph[nowx][nowy] = way[move.index(i)]
                continue
            if graph[nextx][nexty] == '.':
                graph[nowx][nowy] = '.'
                graph[nextx][nexty] = way[move.index(i)]
                nowx,nowy = nextx,nexty
            else:
                graph[nowx][nowy] = way[move.index(i)]
    print(f"#{test_case}",end=' ')
    for i in graph:
        for j in i:
            print(j,end='')
        print()
# #1 **....v
# .-..#..
# #......