# 이것이 취업을 위한 코딩 테스트다.
# 8-7.py를 참고하였습니다.

import sys

input = sys.stdin.readline

N = int(input())  # N * 2


def get_tile_comb(n: int):
    tile = [0] * 3
    tile[1] = 1
    tile[2] = 3

    for i in range(3, n + 1):
        tile.append(tile[i - 2] * 2 + tile[i - 1])  # 1x2는 결국 tile[i-1]에 포함된다.

    return tile[n]


print("최대 타일 조합의 수 : {}".format(get_tile_comb(N)))

