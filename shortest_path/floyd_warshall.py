# 4 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[float("inf")] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    f, t, c = map(int, input().split())
    graph[f][t] = c
for i in range(1, N + 1):
    graph[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, N + 1):
    print(graph[i][1:])
