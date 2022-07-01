import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[float("inf")] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    f, t = map(int, input().split())
    graph[f][t] = 1
    graph[t][f] = 1

for i in range(1, N + 1):
    graph[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

x, k = map(int, input().split())

ans = graph[1][k] + graph[k][x] # 1 -> k -> x
print("{}".format(-1 if ans == float("inf") else ans))

# input sample 1
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# input sample 2
# 4 2
# 1 3
# 2 4
# 3 4
