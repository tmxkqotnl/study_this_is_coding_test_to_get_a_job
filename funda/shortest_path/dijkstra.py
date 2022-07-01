# input sample
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())

graph:list[list[tuple[int,int]]] = [[] for _ in range(n + 1)]
for _ in range(m):
    f, t, d = map(int, input().split())
    graph[f].append((t, d))


def dijkstra(start: int):
    global graph

    dis = [float("inf") for _ in range(n + 1)]
    dis[start] = 0

    q = []
    heapq.heappush(q, (start, 0))

    while q:
        item:tuple[int,int] = heapq.heappop(q)
        cur_pos, cur_cost = item

        if dis[cur_pos] < cur_cost:
            continue

        for next_node, next_cost in graph[cur_pos]:
            cost = cur_cost + next_cost

            if cost < dis[next_node]:
                dis[next_node] = cost
                heapq.heappush(q, (next_node, cost))

    return dis


print(dijkstra(start))


