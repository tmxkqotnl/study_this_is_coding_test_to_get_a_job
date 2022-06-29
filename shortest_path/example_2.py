# input sample
# 3 2 1
# 1 2 4
# 1 3 2

import sys
import heapq

input = sys.stdin.readline


def dijkstra(g: list[list[tuple[int, int]]], start: int):
    global N

    dis = [float("inf")] * (N + 1)
    dis[start] = 0

    q = []
    heapq.heappush(q, (start, 0))
    while q:
        item: tuple[int, int] = heapq.heappop(q)
        cur_pos, cur_cost = item

        if dis[cur_pos] < cur_cost:
            continue

        for next_pos, next_cost in g[cur_pos]:
            cost = next_cost + cur_cost
            if cost < dis[next_pos]:
                dis[next_pos] = cost
                heapq.heappush(q, (next_pos, cost))

    return dis


N, M, C = map(int, input().split())

g: list[list[tuple[int, int]]] = [[] for _ in range(N + 1)]
for _ in range(M):
    f, t, c = map(int, input().split())
    g[f].append((t, c))


ans = dijkstra(g, C)
ans = list(filter(lambda x: x != float("inf"), ans))
print("{} {}".format(len(ans) - 1, max(ans)))  # 자신을 제외한 나머지

