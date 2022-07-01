import sys

input = sys.stdin.readline


def record_operation(n: int):
    global one_cache

    one_cache[n] = one_cache[n - 1] + 1
    if n % 2 == 0:
        one_cache[n] = min(one_cache[n], one_cache[n // 2] + 1)
    elif n % 3 == 0:
        one_cache[n] = min(one_cache[n], one_cache[n // 3] + 1)
    elif n % 5 == 0:
        one_cache[n] = min(one_cache[n], one_cache[n // 5] + 1)


def count_main(n: int):
    for i in range(2, n + 1):
        record_operation(i)

    return one_cache[n]


N = int(input())
one_cache = [0] * (N + 1)

print("최소 연산 횟수 : {}".format(count_main(N)))

