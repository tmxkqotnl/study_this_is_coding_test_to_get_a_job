import sys
from random import randrange

N = int(sys.stdin.readline())
lst = [randrange(1, N, 1) for _ in range(N)]

print("정렬 전 : {}".format(lst))

count = [0] * (N + 1)
for i in lst:
    count[i] += 1
ans = [str(i) * count[i] for i in range(N + 1)]

print("정렬 후 : {}".format("".join(ans)))
