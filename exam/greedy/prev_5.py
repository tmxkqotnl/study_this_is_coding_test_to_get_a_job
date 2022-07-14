from itertools import combinations


def solution(n: int, m: int, lst: list[int]):
    ans = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] != lst[j]:
                ans += 1

    return ans


print("answer 1 : {}".format(solution(5, 3, [1, 3, 2, 3, 2])))
print("answer 2 : {}".format(solution(8, 5, [1, 5, 4, 3, 2, 4, 5, 2])))

