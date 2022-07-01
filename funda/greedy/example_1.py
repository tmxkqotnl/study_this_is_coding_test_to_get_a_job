import sys

input = sys.stdin.readline

N = int(input())
coins = [500, 100, 50, 10]


def get_minimum_coin(n: int):
    global coins

    ans = 0
    for i in coins:
        ans += n // i
        n %= i

    return ans


print("필요한 동전의 최소 갯수 : {}개".format(get_minimum_coin(N)), file=sys.stdout)
