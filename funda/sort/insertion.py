import sys
from random import shuffle

input = sys.stdin.readline

N = int(input())
lst = [_ for _ in range(1, N + 1)]
shuffle(lst)

print("정렬 전 : {}".format(lst))

# insert sort
for i in range(1, N):
    # i 번째 원소의 적절한 위치를 찾는다.
    j = i 
    
    # 위치를 찾을 때까지 반복한다.
    while lst[j] < lst[j - 1] and j >= 1:
        lst[j], lst[j - 1] = lst[j - 1], lst[j]
        j -= 1

print("정렬 후 : {}".format(lst))
