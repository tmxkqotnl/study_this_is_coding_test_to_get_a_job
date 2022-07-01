import sys
from random import shuffle

N = int(sys.stdin.readline())
lst = [_ for _ in range(1, N + 1)]
shuffle(lst)


def merge(left: list[int], right: list[int]) -> list[int]:
    i, j = 0, 0
    s = []

    # 두 리스트를 비교하여 한 리스트에 담는다.
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            s.append(right[j])
            j += 1
        else:
            s.append(left[i])
            i += 1
            
    # 남은 원소를 담는다.
    s += left[i:]
    s += right[j:]

    return s


def merge_sort(lst: list[int]) -> list[int]:
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # 재귀적으로 리스트를 계속해서 반으로 나눈다.
    return merge(merge_sort(left), merge_sort(right))


print("병합 정렬(전) : {}".format(lst))
print("병합 정렬(후) : {}".format(merge_sort(lst)))
