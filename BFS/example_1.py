import sys

input = sys.stdin.readline

N, V = map(int, input().split())
g: list[list[int]] = [list(map(int, input().split())) for _ in range(N + 1)]
visited: list[bool] = [False] * (N + 1)

res: list[int] = []


def dfs(g, v, visited):
    global res

    q = [v]
    visited[v] = True

    while q:
        idx = q.pop(0)
        res.append(idx)
        for i in g[idx]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


dfs(g, V, visited)
print(res)
