import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))


def get_big_number(arr: list[int]):
    global N
    global M
    global K

    arr.sort(reverse=True)

    fst, snd = arr[0], arr[1]
    k_p = K + 1

    q = M // k_p
    s = M % k_p

    return fst * s + (fst * K + snd) * q


print("큰 수 : {}".format(get_big_number(arr)), file=sys.stdout)
