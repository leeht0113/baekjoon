# 단지번호붙이기
import sys
input = sys.stdin.readline
n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]

total = []
visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global area
    area += 1
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x >= 0  and new_x < n and new_y >= 0 and new_y < n:
            if map[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                visited[new_x][new_y] = 1
                dfs(new_x, new_y)

for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            area = 0
            dfs(i, j)
            total.append(area)
total.sort()
print(len(total))
for i in total:
    print(i)
