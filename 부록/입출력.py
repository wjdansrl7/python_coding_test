# 입출력
import sys

# 입력을 위한 전형적인 소스코드
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# 5
# 65 90 75 34 99
# [99, 90, 75, 65, 34]

# 공백을 기준으로 구분하여 적은 수의 데이터 입력
# n, m, k를 공백으로 구분하여 입력
s, m, k = map(int, input().split())

print(s, m, k)

# 3 5 7
# 3 5 7

# C/C++ cin보다 scanf 사용

# 파이썬도 입력의 개수가 많은 경우, 단순히 input()함수를 사용x
# input() 함수는 동작 속도가 느려서 시간초과 날 확률
# sys.stdin.readline()

# 공백 문자를 제거하기 위해서 rstrip()함수 사용
sys.stdin.readline().rstrip()

# readline() 사용 소스코드 예시
# 문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)

# Hello World
# Hello World

# 출력 시 오류가 발생하는 소스코드 예시
# 출력할 변수들
answer = 7

# print("정답은" + answer + "입니다.") => 에러

print("정답은", answer, "입니다.")
print("정답은" + str(answer) + "입니다.")
print(f"정답은 {answer} 입니다.") # python3.6 이상 f-string 문법




