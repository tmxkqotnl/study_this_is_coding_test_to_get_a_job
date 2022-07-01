# input sample 1
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

# input sample 2
# 3 3
# 1 2
# 1 3
# 2 3


import sys

input = sys.stdin.readline

v, e = map(int, input().split())


def find_root(parent: list[int], v: int) -> int:
    return v if parent[v] == v else find_root(parent, parent[v])


def union_parent(parent: list[int], a: int, b: int):
    a = find_root(parent, a)
    b = find_root(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def set_parent(edge_info: list[list[int]], v: int):
    parent = [i for i in range(v + 1)]
    for f, t in edge_info:
        union_parent(parent, f, t)
    return parent


def set_parent_with_cycle_check(edge_info: list[list[int]], v: int):
    parent = [i for i in range(v + 1)]
    for f, t in edge_info:
        if parent[f] == parent[t]:
            return True
        else:
            union_parent(parent, f, t)
    return parent


edges = [list(map(int, input().split())) for _ in range(e)]


print(set_parent(edges, v))
print(set_parent_with_cycle_check(edges, v))
