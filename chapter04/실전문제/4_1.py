# 왕실의 나이트

# location = input()
# x = location[0]
# y = location[1]
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# move_types = ['L', 'R', 'U', 'D']
#
# nx, ny = 0, 0
# for i in range(len(move_types)):
#     nx = x + dx[i]
#     ny = y + dy[i]


# dx[2] + dx[2] + dy[0] UUL
# dx[2] + dx[2] + dy[1] UUR
# dx[3] + dx[3] + dy[0] DDL
# dx[3] + dx[3] + dy[1] DDR
# dy[0] + dy[0] + dx[2] LLU
# dy[0] + dy[0] + dx[3] LLD
# dy[1] + dy[1] + dx[2] RRU
# dy[1] + dy[1] + dx[3] RRD


# 답안

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
