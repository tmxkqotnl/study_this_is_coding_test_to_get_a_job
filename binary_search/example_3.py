# input sample
# 4 6
# 19 15 10 17

import sys
from typing import Optional

input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

max_len = max(lst)


def get_total_len(lst: list[int], val: int) -> int:
    return sum(map(lambda x: x - val if x > val else 0, lst))


def find_minimum_value(
    lst: list[int], min_v: int, left: int, right: int
) -> Optional[int]:
    if left >= right:
        return left

    mid = (left + right) // 2
    cur_total_len = get_total_len(lst, mid)

    if cur_total_len == min_v:
        return mid
    elif cur_total_len > min_v:
        return find_minimum_value(lst, min_v, mid + 1, right)
    else:
        return find_minimum_value(lst, min_v, left, mid - 1)


print("최소값 : {}".format(find_minimum_value(lst, M, 0, max_len)))

