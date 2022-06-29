# 이것이 취업을 위한 코딩 테스트다. 
# 8-8.py를 참고하였습니다.

import sys
from typing import Union

input = sys.stdin.readline

N, M = map(int, input().split())
coins = sorted([int(input()) for _ in range(N)])


def get_coin_num(coins: list[int], m: int) -> Union[int, float]:
    inf_num = float("inf")
    c = [inf_num] * (m + max(coins))
    c[0] = 0

    for i in coins:
        for j in range(i, m + 1):
            if c[j - i] != float("inf"):
                c[j] = min(c[j - i] + 1, c[j])

    return -1 if c[m] == inf_num else c[m]


print("필요한 최소한의 동전 갯수 : {}".format(get_coin_num(coins, M)))

