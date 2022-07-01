import sys

input = sys.stdin.readline

N = int(input())
grades = [input().split() for _ in range(N)]
grades.sort(key=lambda x: int(x[1]))

print("점수를 기준으로 오름차순 정렬 : {}".format(grades))

