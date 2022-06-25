import sys

input = sys.stdin.readline

N, V = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N + 1)]
visited = [False] * (N + 1)

res: list[int] = []


def dfs(g: list[list[int]], v: int, visited: list[bool]):
    global res
    
    visited[v] = True
    res.append(v)
    for i in g[v]:
        if not visited[i]:
            dfs(g, i, visited)


dfs(g, V, visited)
print(res)
