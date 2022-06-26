import sys
from random import shuffle

input = sys.stdin.readline

N = int(input())
lst = [_ for _ in range(1, N + 1)]
shuffle(lst)

print("정렬 전 : {}".format(lst))

# quick sort
def quick_sort(lst: list[int], left: int, right: int):
    if left >= right:
        return

    pivot = left
    i = left + 1
    j = right

    while i <= right and j > left and i <= j:
        # 왼쪽에서부터 pivot보다 큰 값을 찾는다.
        while i <= right and lst[pivot] >= lst[i]:
            i += 1
        # 오른쪽에서부터 pivot보다 작은 값을 찾는다.
        while j > left and lst[pivot] <= lst[j]:
            j -= 1

        # i와 j가 교차하지 않았다면 서로의 위치를 바꾼다.
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    # j 위치를 기준으로 왼쪽에는 pivot보다 작은 값이, 오른쪽에는 큰 값이 위치한다.
    lst[pivot], lst[j] = lst[j], lst[pivot]

    # pivot의 알맞은 위치를 구했으므로, 나머지 원소에 대한 위치를 찾아준다.
    quick_sort(lst, left, j - 1)
    quick_sort(lst, j + 1, right)


quick_sort(lst, 0, N - 1)
print("정렬 후 : {}".format(lst))
