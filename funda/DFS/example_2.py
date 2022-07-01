# input sample 1
# 4 5
# 0 0 1 1 0
# 0 0 0 1 1
# 1 1 1 1 1
# 0 0 0 0 0

# input sample 2
# 15 14
# 0 0 0 0 0 1 1 1 1 0 0 0 0 0
# 1 1 1 1 1 1 0 1 1 1 1 1 1 0
# 1 1 0 1 1 1 0 1 1 0 1 1 1 0
# 1 1 0 1 1 1 0 1 1 0 0 0 0 0
# 1 1 0 1 1 1 1 1 1 1 1 1 1 1
# 1 1 0 1 1 1 1 1 1 1 1 1 0 0
# 1 1 0 0 0 0 0 0 0 1 1 1 1 1
# 0 1 1 1 1 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0 1 1 1 1 1
# 0 1 1 1 1 1 1 1 1 1 1 0 0 0
# 0 0 0 1 1 1 1 1 1 1 1 0 0 0
# 0 0 0 0 0 0 0 1 1 1 1 0 0 0
# 1 1 1 1 1 1 1 1 1 1 0 0 1 1
# 1 1 1 0 0 0 1 1 1 1 1 1 1 1
# 1 1 1 0 0 0 1 1 1 1 1 1 1 1


import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]


def dfs(g: list[list[int]], x: int, y: int):
    global N, M

    if x < 0 or x >= M or y < 0 or y >= N:
        return
    elif g[y][x] == 1:
        return

    g[y][x] = 1
    dfs(g, x + 1, y)
    dfs(g, x - 1, y)
    dfs(g, x, y + 1)
    dfs(g, x, y - 1)


def counter():
    count = 0

    while True:
        count += 1
        yield count


def dfs_main(g):
    copied = copy.deepcopy(g)
    gen = counter()

    for i in range(N):
        for j in range(M):
            if copied[i][j] == 0:
                dfs(copied, j, i)
                next(gen)

    return next(gen) - 1


print(dfs_main(g), file=sys.stdout)

