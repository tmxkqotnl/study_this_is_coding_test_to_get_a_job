# input sample
# 5
# 8 3 7 9 2
# 3
# 5 7 9


import sys

input = sys.stdin.readline


def b_search_recursive(lst: list[int], target: int) -> str:
    if not lst:
        return "no"

    mid = (len(lst) - 1) // 2
    if lst[mid] == target:
        return "yes"
    elif lst[mid] > target:
        return b_search_recursive(lst[:mid], target)
    else:
        return b_search_recursive(lst[mid + 1 :], target)


def find_all(container: list[int], target_lst: list[int]) -> list[str]:
    return [b_search_recursive(container, i) for i in target_lst]


N = int(input())
n_lst = sorted(list(map(int, input().split())))

M = int(input())
m_lst = list(map(int, input().split()))

print("모든 아이템이 있는가? - {}".format(" ".join(find_all(n_lst, m_lst))))

