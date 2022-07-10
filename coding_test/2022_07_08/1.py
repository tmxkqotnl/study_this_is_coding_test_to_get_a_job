# https://www.geeksforgeeks.org/find-the-size-of-largest-subset-with-positive-bitwise-and/


def solution(A):
    A = map(lambda x: list(reversed(format(x, "b"))), A)
    bits = [0] * (1000000000).bit_length()

    for i in A:
        for j in range(len(i)):
            bits[j] += int(i[j])
    return max(bits)
