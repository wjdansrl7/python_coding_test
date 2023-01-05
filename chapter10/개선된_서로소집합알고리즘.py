# 기존의 서로소집합 알고리즘을 사용하면 find_parent()에서 루트 노드를 찾기 위해서, 최악의 경우 시간 복잡도 O(V)을 가지게 된다.
# 결과적으로 현재의 알고리즘을 그대로 이용하게 되면 노드의 개수가 V개이고 find 혹은 union 연산의 개수가 M개일 때, 전체 시간 복잡도는 O(VM)이 되어
# 비효율적이다.
# 하지만 이러한 find 함수는 아주 간단한 과정으로 최적화가 가능하다. 바로 경로 압축(Path Compression)기법을 적용하면 시간 복잡도를 계산할 수 있다.

# 개선된 서로소 집합 알고리즘 소스코드

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    else:
        return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(Union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합:', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블:', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')

