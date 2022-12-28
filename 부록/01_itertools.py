# 표준 라이브러리 : 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해놓은 라이브러리

# 내장 함수 : print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을
# 포하하고 있는 기본 내장 라이브러리이다. 파이썬 프로그램을 작성할 때 없어서는 안되는 필수적인 기능을 포함하고 있다.
# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리이다.
# 순열과 조합 라이브러리를 제공한다.
# heapq : 힙(Heap) 기능을 제공하는 라이브러리이다. 우선순위 큐 기능을 구현하기 위해 사용한다.
# bisect : 이진 탐색(Binary Search) 기능을 제공하는 라이브러리이다.
# collections : 덱(dequeue), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리이다.
# math : 필수적인 수학적 기능을 제공하는 라이브러리이다. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련
# 함수부터 파이(pi)와 같은 상수를 포함하고 있다.

result = sum([1, 2, 3, 4, 5])
print(result)

result = min(7, 3, 5, 2)
print(result)

result = max(7, 3, 5, 2)
print(result)

# eval() 함수 : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환
result = eval("(3 + 5) * 7")
print(result)

result = sorted([9, 1, 8, 5, 4])
print(result)
result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)

result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key=lambda x: x[1],
                reverse=True)
print(result)

# 리스트와 같은 iterable 객체는 기본으로 sort() 함수를 내장

data = [9,1,8,5,4]
data.sort()
print(data)

from itertools import permutations, combinations, product
# itertools은 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다.

# permutations, combinations, product 모두 클래스이므로 객체 초기화 이후에는 리스트 자료형으로
# 변환하여 사용한다.

# permutations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일열로 나열하는
# 모든 경우(순열)를 계산해준다.

data = ['A', 'C', 'B']  # 데이터 준비
result = list(permutations(data, 2))  # 모든 순열 구하기

print(result)


# combinations은 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고
# 나열하는 모든 경우(조합)을 계산한다
result = list(combinations(data, 2))  # 2개를 뽑는 모든 조합 구하기
print(result)

# product는 permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로
# 나열하는 모든 경우(순열)을 계산한다.
data = ['A', 'B','C']
result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)

from itertools import combinations_with_replacement
# combinations_with_replacement는 combinations와 같이 리스트와 같은
# iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)을 계산한다.

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)

