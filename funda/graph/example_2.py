# input sample
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4

import sys

input = sys.stdin.readline


def find_parent(parent: list[int], v: int) -> int:
    return v if parent[v] == v else find_parent(parent, parent[v])


def union_parent(parent: list[int], v1: int, v2: int):
    v1 = find_parent(parent, v1)
    v2 = find_parent(parent, v2)

    if v1 > v2:
        parent[v1] = v2
    else:
        parent[v2] = v1


def get_minimum_cost(edges: list[list[int]], vertex: int) -> int:
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(vertex + 1)]

    cost: list[int] = []
    for f, t, c in edges:
        if find_parent(parent, f) != find_parent(parent, t):
            union_parent(parent, f, t)
            cost.append(c)

    return sum(cost[:-1])


v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]

print("최소 비용 : {}".format(get_minimum_cost(edges, v)))
