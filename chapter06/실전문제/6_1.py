
# 위에서 아래로
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for i in range(len(array)):
    print(array[i], end=' ')

# 답안

# N을 입력받기
n = int(input())

# N개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

# 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')



