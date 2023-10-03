# 연결 요소의 개수
import sys
# sys.setrecursionlimit(10 ** 6)
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# def dfs(graph, v, visited):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

answer = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        # dfs(graph, i, visited)
        answer += 1

print(answer)