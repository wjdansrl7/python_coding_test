# bisect
# 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공한다.
# bisect 라이브러리는 "정렬된 배열"에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다.

# 시간복잡도: O(logN)
# bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
