# 거스름돈
# 내가 푼 문제

# charge = int(input())
#
# a = int(charge / 500)
# charge -= a * 500
#
# b = int(charge / 100)
# charge -= b * 100
#
#
# c = int(charge / 50)
# charge -= c * 50
#
# d = int(charge / 10)
#
# print(a + b + c + d)

# 답안

n = 1260
count = 0
# 큰 단위의 화폐부터 차례대로 확인
count_types = [500, 100, 50, 10]

for coin in count_types:
    count += n / coin
    n %= coin

print(count)




