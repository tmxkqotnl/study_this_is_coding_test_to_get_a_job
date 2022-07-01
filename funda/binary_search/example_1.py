import sys
from random import randrange
from typing import Optional

input = sys.stdin.readline


def binary_search_recursive(
    lst: list[int], left: int, right: int, target: int
) -> Optional[int]:
    if not lst:
        return None

    mid = (left + right) // 2

    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search_recursive(lst, left, mid - 1, target)
    else:
        return binary_search_recursive(lst, mid + 1, right, target)


def binary_search_iterative(
    lst: list[int], left: int, right: int, target: int
) -> Optional[int]:
    while lst:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            right = mid - 1
        else:
            left = mid + 1


def binary_search_main():
    N = int(input())
    lst = sorted([randrange(1, 100) for _ in range(N)])
    target_idx = randrange(N)

    print("검색 대상 : {}, 타겟 : {}, 타겟 인덱스 : {}".format(lst, lst[target_idx], target_idx))

    ans = binary_search_recursive(lst, 0, len(lst) - 1, lst[target_idx])
    if ans:
        print("재귀적 이진 탐색 - 타겟 인덱스 : {}".format(ans))

    ans = binary_search_iterative(lst, 0, len(lst) - 1, lst[target_idx])
    if ans:
        print("순차 이진 탐색 - 타겟 인덱스 : {}".format(ans))


binary_search_main()
