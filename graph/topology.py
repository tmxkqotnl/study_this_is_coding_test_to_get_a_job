# input sample
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

import sys

input = sys.stdin.readline

v, e = map(int, input().split())
indegree = [0] * (v + 1)

g: list[list[int]] = [[] for i in range(v + 1)]
for _ in range(e):
    f, t = map(int, input().split())

    g[f].append(t)
    indegree[t] += 1


def topology_sort(graph: list[list[int]], indegree: list[int]) -> list[int]:
    q = []
    q.append(indegree.index(0,1))

    order = []
    while q:
        cur: int = q.pop(0)
        order.append(cur)

        for i in graph[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return order


print("result : {}".format(topology_sort(g, indegree)))