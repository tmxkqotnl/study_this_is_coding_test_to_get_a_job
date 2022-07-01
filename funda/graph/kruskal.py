# input sample
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25

import sys

input = sys.stdin.readline

v, e = map(int, input().split())
edges: list[list[int]] = [list(map(int, input().split())) for _ in range(e)]
edges.sort(key=lambda x: x[2])


def find_parent(parent: list[int], v: int) -> int:
    return v if parent[v] == v else find_parent(parent, parent[v])


def union_parent(parent: list[int], v1: int, v2: int):
    v1 = find_parent(parent, v1)
    v2 = find_parent(parent, v2)

    if v1 > v2:
        parent[v1] = v2
    else:
        parent[v2] = v1


def kruskal(edges: list[list[int]], v: int) -> int:
    parent = [i for i in range(v + 1)]

    uncycled = []
    for f, t, c in edges:
        if find_parent(parent, f) != find_parent(parent, t):
            union_parent(parent, f, t)
            uncycled.append(c)

    return sum(uncycled)


print("total cost : {}".format(kruskal(edges, v)))
