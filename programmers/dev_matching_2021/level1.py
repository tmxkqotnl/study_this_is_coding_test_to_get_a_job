# test : 로또의 최고 순위와 최저 순위
# link : https://programmers.co.kr/learn/courses/30/lessons/77484


def solution(lottos: list[int], win_nums: list[int]):
    numbers = [0]*46

    for i in range(6):
        numbers[lottos[i]] += 1
        numbers[win_nums[i]] += 1

    wins = len(list(filter(lambda x: x == 2, numbers[1:])))
    zeros = numbers[0]

    minimum_rank = 7 - wins if wins >= 2 else 6
    max_rank = 7 - wins - zeros if wins + zeros >= 2 else 6

    return [max_rank, minimum_rank]
