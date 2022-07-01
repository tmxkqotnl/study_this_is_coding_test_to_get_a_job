import sys
from random import shuffle

input = sys.stdin.readline

N = int(input())
lst = [_ for _ in range(1, N + 1)]
shuffle(lst)

print("정렬 전 : {}".format(lst))

# selection sort
for i in range(N - 1):
    # i 번째 위치에 올 가장 작은 원소를 찾는다.
    idx = i
    for j in range(i + 1, N):
        if lst[idx] > lst[j]:
            idx = j

    lst[i], lst[idx] = lst[idx], lst[i]

print("정렬 후 : {}".format(lst))
