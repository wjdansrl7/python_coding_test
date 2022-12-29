# 미로 탈출

# from collections import deque
#
# n, m = map(int, input().split())
#
# array = []
# for i in range(n):
#     array.append(list(map(int, input())))
#
# visited = [[False] * m for _ in range(n)]
#
# dx = [-1, 0, 1, 0]  # 북, 서, 남, 동
# dy = [0, -1, 0, 1]  # 북, 서, 남, 동
#
# count = 1
#
#
# def bfs(graph, start_x, start_y, visited):
#     global count
#     queue = deque([(start_x, start_y)])
#     visited[start_x][start_y] = True
#
#     while queue:
#         x, y = queue.popleft()
#         t = 0
#         print(x, y)
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 t += 1
#                 if t == 4:
#                     count -= 1
#                 continue
#             if (not visited[nx][ny]) and graph[nx][ny] == 1:
#                 visited[nx][ny] = True
#                 queue.append((nx, ny))
#                 count += 1
#             else:
#                 t += 1
#                 if t == 4:
#                     count -= 1
#
# bfs(array, 0, 0, visited)
# print(count)

from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]


# BFS를 수행한 결과 출력
print(bfs(0, 0))
