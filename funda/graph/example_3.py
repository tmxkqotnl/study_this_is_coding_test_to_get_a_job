# input sample
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

import sys
import copy

input = sys.stdin.readline

N: int = int(input())
course: list[list[int]] = [list(map(int, input().split())) for _ in range(N)]

cost: list[int] = [0]
g: list[list[int]] = [[] for _ in range(N + 1)]
indegree: list[int] = [0] * (N + 1)

for i in range(N):
    cost.append(course[i][0])
    for j in course[i][1:]:
        if j != -1:
            g[j].append(i + 1)
            indegree[i + 1] += 1


def topology(graph: list[list[int]], indegree: list[int], cost: list[int]):
    # find start index
    start_index = indegree.index(0, 1)
    q = [start_index]

    real_cost = copy.deepcopy(cost)
    while q:
        cur = q.pop(0)
        for i in graph[cur]:
            indegree[i] -= 1
            real_cost[i] = max(real_cost[i], real_cost[cur] + cost[i]) # 10-9.py 답안 참고
            if indegree[i] == 0:
                q.append(i)

    return real_cost


print(*topology(g, indegree, cost)[1:])

