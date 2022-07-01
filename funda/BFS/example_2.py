# input sample 1
# 3 3
# 1 1 0
# 0 1 0
# 0 1 1

# input sample 2
# 5 6
# 1 0 1 0 1 0
# 1 1 1 1 1 1
# 0 0 0 0 0 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]


def directions():
    yield from [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(g: list[list[int]], s_x: int, s_y: int):
    global M
    global N

    g[s_y][s_x] = 1
    q = [(s_x, s_y)]

    while q:
        cur_x, cur_y = q.pop(0)
        for i, j in directions():
            dx = cur_x + i
            dy = cur_y + j

            if dx == M - 1 and dy == N - 1:
                return g[cur_y][cur_x] + 1

            # 시작점을 제외시켜주지 않으면 불필요한 연산이 추가되지만, 조건식 하나가 줄어듦
            if dx >= M or dx < 0 or dy >= N or dy < 0:
                continue
            if g[dy][dx] != 1:
                continue

            q.append((dx, dy))
            g[dy][dx] = g[cur_y][cur_x] + 1


print("최단거리 : {}".format(bfs(g, 0, 0)))

