from functools import reduce


def solution(s: str):
    return reduce(lambda acc, cur: max(acc * cur, acc + cur), map(int, list(s)))


print("answer 1 : {}".format(solution("02984")))
print("answer 2 : {}".format(solution("567")))

