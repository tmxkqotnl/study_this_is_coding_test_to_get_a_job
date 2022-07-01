import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # row, col
ans = max([min(map(int, input().split())) for i in range(N)])

print("가장 작은 값들 중 가장 큰 값 : {}".format(ans), file=sys.stdout)
