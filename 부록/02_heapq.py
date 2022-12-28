# heapq
# heapq는 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을
# 구현하고자 할때 사용된다.
# heapq > priorityQueue : 더 빠름

# 파이썬의 heap은 최소 힙(Min Heap)으로 구성되어 있으므로 단순히 원소를 힙에 전부 넣었다가
# 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다. 보통 최소 힙 자료구조의
# 최상단 원소는 항상 '가장 작은' 원소이기 때문이다.

# 힙에 원소를 삽입할 때에는 heapq.heappush(), 원소를 꺼내고자 할 때에는 heapq.heappop()

import heapq


def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


# 파이썬에서는 최대 힙(Max Heap)을 제공하지 않는다. 따라서 heapq 라이브러리를 이용하여 최대 힙을 구현해야 할때에는
# 원소의 부호를 임시로 변경하는 방식을 이용한다.

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
