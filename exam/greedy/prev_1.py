import sys

def solution(n: int, lst: list[int]):
    lst = sorted(lst, reverse=True)

    ans = 0
    for i in lst:
        if n < i:
            return ans
        n -= i
        ans += 1


n = 5
lst = [2, 3, 1, 2, 2]

print("answer : {}".format(solution(n, lst)))
