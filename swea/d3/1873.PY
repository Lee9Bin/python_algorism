t = int(input())

for tc in range(t):
    h, w = map(int, input().split())

    graph = []

    for i in range(h):
        graph.append(list(map(str, input().rstrip())))
    tank = ["^", "v", "<", ">"]
    nowx, nowy = 0, 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] in tank:
                nowx, nowy = i, j

    n = int(input())
    command = list(map(str, input().rstrip()))

    for i in command:
        if i == "U":
            graph[nowx][nowy] = "^"
            if nowx-1 >= 0 and nowy >=0 and nowx-1 < h and nowy < w:
                if graph[nowx-1][nowy] == ".":
                    graph[nowx][nowy] = "."
                    nowx, nowy = nowx-1, nowy
                    graph[nowx][nowy] = "^"
        if i == "D":
            graph[nowx][nowy] = "v"
            if nowx+1 >= 0 and nowy >=0 and nowx+1 < h and nowy < w:
                if graph[nowx + 1][nowy] == ".":
                    graph[nowx][nowy] = "."
                    nowx, nowy = nowx + 1, nowy
                    graph[nowx][nowy] = "v"
        if i == "L":
            graph[nowx][nowy] = "<"
            if nowx >= 0 and nowy-1 >=0 and nowx < h and nowy-1 < w:
                if graph[nowx][nowy-1] == ".":
                    graph[nowx][nowy] = "."
                    nowx, nowy = nowx, nowy-1
                    graph[nowx][nowy] = "<"
        if i == "R":
            graph[nowx][nowy] = ">"
            if nowx >= 0 and nowy+1 >=0 and nowx < h and nowy+1 < w:
                if graph[nowx][nowy+1] == ".":
                    graph[nowx][nowy] = "."
                    nowx, nowy = nowx, nowy+1
                    graph[nowx][nowy] = ">"

        if i == "S":
            if graph[nowx][nowy] == "^":
                dx, dy = -1, 0
            if graph[nowx][nowy] == "v":
                dx, dy = 1, 0
            if graph[nowx][nowy] == "<":
                dx, dy = 0, -1
            if graph[nowx][nowy] == ">":
                dx, dy = 0, 1
            nextx = nowx
            nexty = nowy
            while True:
                nextx += dx
                nexty += dy

                if nextx < 0 or nexty < 0 or nextx >= h or nexty >= w or graph[nextx][nexty] == "#":
                    break
                if graph[nextx][nexty] == "*":
                    graph[nextx][nexty] = "."
                    break
    print(f"#{tc+1}", end=" ")
    for i in range(h):
        for j in range(w):
            print(graph[i][j],end="")
        print()