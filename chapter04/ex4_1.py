# 상하좌우

N = int(input())
x, y = 1, 1

m = map(str, input().split())

for i in m:
    if i == 'R':
        if y+1 > N:
            continue
        y += 1
    if i == 'L':
        if y - 1 < 1:
            continue
        y -= 1
    if i == 'D':
        if x+1 > N:
            continue
        x += 1
    if i == 'U':
        if x - 1 < 1:
            continue
        x -= 1

print(x, y)

# 답안
# N을 입력받기
n = int(input())

x,y = 1,1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0,0, -1, 1]
dy = [-1, 1, 0,0]
move_types = ['L', 'R', 'U', 'D']

nx, ny = 0, 0
# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
        # 이동 수행
    x, y = nx, ny

print(x, y)



