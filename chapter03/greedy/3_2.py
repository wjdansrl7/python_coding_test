# 큰 수의 법칙
# 내가 푼 풀이

# N, M, K = input().split()
#
# N = int(N)
# M = int(M)
# K = int(K)
#
# array = []
# a = input().split()
#
# for i in range(len(a)):
#     b = int(a[i])
#     array.append(b)
#
# # array = [2, 4, 5, 4, 6]
#
# array.sort(reverse=True)
# print(array)
#
# sum = 0
# count = 0
# while M > 0:
#     sum += array[0]
#     count += 1
#     M -= 1
#     if count % 3 == 0:
#         sum += array[1]
#         M -= 1
#
# print(sum)

# 문제 해설

# N, M, K를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split())
# # N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))
#
# data.sort()  # 입력받은 수를 정렬하기
# first = data[n-1]
# second = data[n-2]
#
# result = 0
#
# while True:
#     for i in range(k):  # 가장 큰 수를 K번 더하기
#         if m == 0:  # m이 0이라면 반복문 탈출
#             break
#         result += first
#         m -= 1  # 더핳 때마다 1씩 빼기
#     if m == 0:  # m이 0이라면 반복문 탈출
#         break
#     result += second  # 두 번째로 큰 수를 한 번 더하기
#     m -= 1  # 더할 때마다 1씩 빼기
#
# print(result)  # 최종 답안 제출

# 수열을 이용한 풀이
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력 받은 수 정렬
first = data[n-1]
second = data[n-2]

# 가장 많은 수가 더해지는 횟수 계산

count = int(m/(k+1)) * k
count += m%(k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)

