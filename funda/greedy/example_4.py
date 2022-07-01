import sys

input = sys.stdin.readline

N, K = map(int, input().split())


def recursion_until_be_one(n: int, k: int):
    if n <= 1:
        return 0

    temp = n % k

    if temp != 0:
        print("빼기 {} {}".format(temp, n))
        return (temp if temp != n else temp - 1) + recursion_until_be_one(n - temp, k)
    else:
        print("나누기 {} {}".format(temp, n))
        return 1 + recursion_until_be_one(n // k, k)


print("1이 될때까지 연산 횟수 : {}".format(recursion_until_be_one(N, K)), file=sys.stdout)

