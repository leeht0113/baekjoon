# 미로 탐색
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()
queue.append((0, 0))
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
while queue:
    x, y = queue.popleft()
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
            if visited[new_x][new_y] == 0 and graph[new_x][new_y] != 0:
                 queue.append((new_x, new_y))
                 visited[new_x][new_y] = visited[x][y] + 1            
print(visited[n-1][m-1])