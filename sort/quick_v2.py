# 이것이 취업을 위한 코딩 테스트다. 예제 코드 6-5.py 를 참고하였습니다.

import sys
from random import shuffle

input = sys.stdin.readline

N = int(input())
lst = [_ for _ in range(1, N + 1)]
shuffle(lst)

print("정렬 전 : {}".format(lst))


def quick(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    last = lst[1:]

    left_side = [x for x in last if x <= pivot]
    right_side = [x for x in last if x > pivot]

    return quick(left_side) + [pivot] + quick(right_side)


print("정렬 후 : {}".format(quick(lst)))
