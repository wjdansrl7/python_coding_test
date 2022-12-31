
# 떡볶이 떡 만들기
n, m = map(int, input().split())

array = list(map(int, input().split()))

# 4, 6
# 19 15 10 17
#  15 => 4 0 0 2

max_a = max(array)
min_a = min(array)
while True:
    result = []
    for i in range(n):
        if array[i] - max_a > 0:
            result.append(array[i] - max_a)
        else:
            result.append(0)

    if sum(result) >= m:
        break
    else:
        max_a -= 1
        if min_a > max_a:
            print('답이 없다.')

print(max_a)

# 답안
# TODO: 파라메트릭 서치(Parametric Search): 최적화 문제를 결정 문제로 바꾸어 해결하는 기법이다.
# TODO: '원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'는 주로 파라메트릭 서치를 이용해 푼다.
# 보통 파라메트릭 서치는 이진 탐색을 이용하여 해결한다. 재귀 함수 기법보다는 반복문을 주로 사용한다.
# 절단기의 높이(탐색 범위)는 1부터 10억까지의 정수 중 하나인데, 이처럼 큰 수를 보면 이진 탐색을 떠올리는 게 좋다.

# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n, m = list(map(int, input().split()))
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    else:
        result = mid  # 최대한 덜 잘랐을 때가 정다빙므로, 여기에서 result에 기록
        start = mid + 1

print(result)



