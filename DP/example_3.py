# 이것이 취업을 위한 코딩 테스트다.
# 8-6.py를 참고하였습니다.

import sys

input = sys.stdin.readline

N = int(input())
warehouse = list(map(int, input().split()))


def get_max_food(w: list[int], n: int):
    m = [0] * 2

    m[0] = w[0]
    m[1] = max(m[0], w[1])

    for i in range(2, n):
        m.append(max(m[i - 1], m[i - 2] + w[i]))

    return m[n - 1]


print("얻을 수 있는 최대 식량의 양 : {}".format(get_max_food(warehouse, N)))

