
# 두 배열의 원소 교체
# TODO: 나는 배열 A에서 가장 작은 원소가 배열 B에서 가장 큰 원소보다 작을 때에만 교체를 수행해야 한다를 고려하지 않음.
n, k = map(int, input().split())


A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()  # 1,2,3,4,5
B.sort(reverse=True)  # 6,6,5,5,5

# for i in range(k):
#     A[i], B[i] = B[i], A[i]

# 수정해봄, but 약간의 시간복잡도에서 아쉬운 점이 있다
for i in range(k):
    for j in range(n):
        if A[i] < B[j]:
            A[i], B[j] = B[j], A[i]

print(sum(A))

# 답안
# 문제에서 두 배열의 원소가 최대 100,000개까지 입력될 수 있으므로 O(NlogN)을 보장하는 정렬 알고리즘을 이용해야 한다.

n, k = map(int, input().split())  # N과 K를 입력받기
a = list(map(int, input().split()))  # 배열 A의 모든 원소를 입력받기
b = list(map(int, input().split()))  # 배열 B의 모든 원소를 입력받기

a.sort()  # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True)  # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:  # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))  # 배열 A의 모든 원소의 합을 출력





