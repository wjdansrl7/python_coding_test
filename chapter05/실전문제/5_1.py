# 음료수 얼려 먹기
# from collections import deque

# dx = [-1, 0, 1, 0]  # 북 동 남 서
# dy = [0, 1, 0, -1]
#
# count = 0
#
#
# def bfs(graph, start_x, start_y, visited):
#     queue = deque[(start_x, start_y)]
#     visited[start_x][start_y] = True
#     global count
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if not visited[nx][ny] and graph[nx][ny] == 0:  # 방문하지 않는 노드이면서 구멍이 뚫려 있는 부분이라면
#                 visited[nx][ny] = True
#                 queue.append((nx, ny))
#     count += 1
#
#
# n, m = map(int, input().split())
#
# array = []
# for i in range(n):
#     array.append(list(map(int, input())))  # 구멍이 뚫려 있는 부분: 0, 칸막이가 존재하는 부분: 1
#
# visited = [[False] * m for _ in range(n)]
#
# # bfs 방식을 이용
#
# for i in range(n):
#     for j in range(m):
#         bfs(array, i, j, visited)
#
# print(count)

# 답안

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1


print(result)

