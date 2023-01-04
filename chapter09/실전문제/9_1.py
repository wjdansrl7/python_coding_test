# 미래 도시

# 나의 답안은 애초에 접근이 잘못됨. 1번 회사에서 K번 회사를 거쳐서 X번 회사로 간다고 할 때,
# 플로이드 워셜 알고리즘의 핵심: 'A에서 B로 가는 최소 비용'과 'A에서 K를 거쳐서 B로 가는 최소 비용' 중에 최소값
# import heapq
# import sys
#
# INF = int(1e9)
#
# # 회사의 개수, 간선의 개수
# n, m = map(int, input().split())
#
# graph = [[] for _ in range(n + 1)]
#
# distance = [INF] * (n + 1)
#
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append((b, 1))
#
# start = 1
#
#
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#
#     while q:
#         dist, now = heapq.heappop(q)
#
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0],))
#
#
# dijkstra(start)

# 답안

INF = int(1e9)  # 무한을 의미하는 값으로 10억으로 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 1

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
    print("-1")
else:
    print(distance)









