from itertools import combinations


def solution(n: int, lst: list[int]):
    numbers = [0 for _ in range(sum(lst) + 2)]

    for i in range(1, len(lst) + 1):
        comb_sum = [sum(i) for i in combinations(lst, i)]
        for j in comb_sum:
            numbers[j] += 1

    return numbers.index(0, 1)


print("answer 1 : {}".format(solution(5, [3, 2, 1, 1, 9])))
print("answer 2 : {}".format(solution(2, [1, 2])))
print("answer 2 : {}".format(solution(2, [3, 5])))

