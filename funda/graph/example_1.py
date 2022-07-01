# input sample
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

import sys

input = sys.stdin.readline

N, M = map(int, input().split())


def find_parent(parent: list[int], v: int) -> int:
    return v if parent[v] == v else find_parent(parent, parent[v])


def union_parent(parent: list[int], v1: int, v2: int):
    v1 = find_parent(parent, v1)
    v2 = find_parent(parent, v2)

    if v1 > v2:
        parent[v1] = v2
    else:
        parent[v2] = v1


def main(n: int,m:int):
    parent = [i for i in range(n + 1)]
    
    ops = [map(int, input().split()) for _ in range(m)]
    for c,f,t in ops:
        if c == 1:
            f = find_parent(parent, f)
            t = find_parent(parent, t)
            if f == t:
                print("YES")
            else:
                print("NO")
        else:
            union_parent(parent, f, t)


main(N,M)
