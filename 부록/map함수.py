# map(function, iterable) 첫 번째 매개변수는 함수, 두 번째 매개변수로는 반복 가능한 자료형(리스트, 튜플 등)
# map 함수의 반환 값은 map 객체 이기 때문에 해당 자료형을 list or tuple로 형 변환시켜주어야 한다.
# 함수의 동작은 두 번째 인자로 들어온 반복 가능한 자료형(리스트나 튜플)을 첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 수행하는 함수
# map(적용시킬 함수, 적용할 값들)

import math

# map 함수를 사용하는 것과 아닌 것의 차이
# 리스트에 값을 하나씩 더해서 새로운 리스트를 만드는 작업
myList = [1, 2, 3, 4, 5]

# for 반복문 이용
result1 = []
for val in myList:
    result1.append(val + 1)

print(f'result1 : {result1}')


# map 함수 이용
def add_one(n):
    return n + 1


result2 = list(map(add_one, myList))
print(f'result2 : {result2}')

# 리스트와 map 함수

# 예제1) 리스트의 값을 정수 타입으로 변환
result1 = list(map(int, [1.1, 2.2, 3.3, 4.4, 5.5]))
print(f'map(int, 리스트) : {result1}')


# 예제2) 리스트 값 제곱
def func_pow(x):
    return pow(x, 5)  # x의 5제곱을 반환


result2 = list(map(func_pow, [1, 2, 3, 4, 5]))
print(f'map(func_pow, 리스트) : {result2}')

# 예제3) 리스트 값 소수점 올림
result3 = list(map(math.ceil, [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]))
print(f'map(func_ceil, 리스트) : {result3}')


# 람다와 map 함수
# map의 첫 번째 인자로 함수가 들어간다면
# 이름없는 함수 즉, 람다 함수도 가능하다는 뜻

# 일반 함수 이용
def func_mul(x):
    return x * 2


result1 = list(map(func_mul, [5, 4, 3, 2, 1]))
print(f"map(일반함수, 리스트) : {result1}")

# 람다 함수 이용
result2 = list(map(lambda x: x * 2, [5, 4, 3, 2, 1]))
print(f"map(람다함수, 리스트) : {result2}")
