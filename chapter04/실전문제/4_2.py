# 게임 개발

# vx, vy = map(int, input().split())
# x, y, location = map(int, input().split())
#
# visited = [[False] * vy for _ in range(vx)]
# # 북: 0, 남: 2, 동: 1, 서: 3
# # L, R, U, D
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
#
# arr = []
# for i in range(vx):
#     arr.append(list(map(int, input().split())))
#
#
# count = 0
# if location == 0:  # U
#     location = 3
#     cx = x + dx[3]
#     cy = y + dy[3]
#     if vx[cx][cx] == 1:
#         x += dx[3]
#         y += dx[3]
#         visited[x][y] = True
#         count += 1
#     else:
#         pass
# elif location == 1:  # R
#     pass
# elif location == 2:  # D
#     pass
# elif location == 3:  # L
#     pass
# else:
#     pass

# 답안

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X좌표, Y좌표, 방향을 입력받기
x, y, directions = map(int, input().split())
d[x][y] = 1  # 현재 방문한 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의 0,1,2,3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def turn_left():
    global directions
    directions -= 1
    if directions == -1:
        directions = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[directions]
    ny = y + dy[directions]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[directions]
        ny = y - dy[directions]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

# 정답 출력
print(count)


