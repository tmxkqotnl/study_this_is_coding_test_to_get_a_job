import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

print("역순 정렬 : {}".format(sorted(nums, reverse=True)))

