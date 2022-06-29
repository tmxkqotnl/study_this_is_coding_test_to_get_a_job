import sys
import time
from typing import Callable

input = sys.stdin.readline


def fibo(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return fibo(n - 1) + fibo(n - 2)


def fibo_memoization(n: int) -> int:
    global fibo_cache

    if fibo_cache[n] == 0:
        fibo_cache[n] = fibo_memoization(n - 1) + fibo_memoization(n - 2)

    return fibo_cache[n]


def check_time(func: Callable[[int], int], n: int):
    start_time = time.time()
    for i in range(n):
        func(i)
    print("execution time : {}".format(time.time() - start_time))


N = int(input())

fibo_cache = [0] * (N + 1)
fibo_cache[0] = 1
fibo_cache[1] = 1

check_time(fibo, 30)  # recommend not to try
check_time(fibo_memoization, N)

