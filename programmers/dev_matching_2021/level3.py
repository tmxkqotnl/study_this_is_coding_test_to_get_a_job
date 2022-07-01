# test : 다단계 칫솔 판매
# link : https://programmers.co.kr/learn/courses/30/lessons/77486
import math


def solution(
    enroll: list[str], referral: list[str], seller: list[str], amount: list[int]
):
    enroll_referral = {enroll[i]: referral[i] for i in range(len(enroll))}
    settlement = {enroll[i]: 0 for i in range(len(enroll))}

    for i in range(len(seller)):
        calculate(seller[i], amount[i] * 100, enroll_referral, settlement)

    return [_ for _ in settlement.values()]


def calculate(
    member: str, amount: int, referral: dict[str, str], settlement: dict[str, int]
):
    one_of_amount = math.floor(amount * 0.1)
    nine_of_amount = amount - one_of_amount

    if one_of_amount < 1:
        settlement[member] += amount
    elif referral[member] == "-":
        settlement[member] += nine_of_amount
    else:
        settlement[member] += nine_of_amount
        calculate(referral[member], one_of_amount, referral, settlement)

