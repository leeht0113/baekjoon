# 그림
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

count = 0
area = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(graph, start, visited):
    area = 1
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
                if graph[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                    area += 1
                    visited[new_x][new_y] = 1
                    queue.append((new_x, new_y))
    return area

visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            area.append(bfs(graph, (i, j), visited))
            count += 1

print(count)
if len(area) > 0:
    print(max(area))
else:
    print(0)