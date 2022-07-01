import sys

input = sys.stdin.readline
N, K = map(int, input().split())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

ans = a[K:] + b[:K]

print("A : {}".format(a))
print("B : {}".format(b))
print("바꿔치기한 결과 : {} / 합 : {}".format(ans,sum(ans)))
