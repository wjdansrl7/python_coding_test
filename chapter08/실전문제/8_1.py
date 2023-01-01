# 1로 만들기

count = 0


def make_1(x):
    global count
    if x == 1:
        return count
    if x % 5 == 0:
        x //= 5
        count += 1
        make_1(x)
    elif x % 3 == 0:
        x //= 3
        count += 1
        make_1(x)
    elif x % 2 == 0:
        x //= 2
        count += 1
        make_1(x)
    else:
        x -= 1
        count+= 1
        make_1(x)


# x = int(input())

# 답안

# 정수 X를 입력받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
