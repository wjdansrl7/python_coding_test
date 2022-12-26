# 게임 개발

vx, vy = map(int, input().split())

vx += 2
vy += 2

x, y, location = map(int, input().split())

dx = [0,0, -1, 1]
dy = [-1, 1, 0, 0]

# L, R, U, D
move_types = [3, 1, 0, 2]

arr = []

for i in range(vx):
    for j in range(vy):
        if i == 0 or i == vx - 1 or j == 0 or j == vy - 1:
            arr[i][j].append(0)
            continue
        arr[i][j].append(list(map(int, input().split())))


for i in range(vx):
    for j in range(vy):
        print(arr[i][j])


