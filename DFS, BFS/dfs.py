adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
adj[2][3] = adj[2][4] = 1
adj[5][6] = 1
adj[7][8] = adj[7][9] = 1
adj[9][10] = adj[9][11] = adj[9][12] = 1
# for row in adj:
#     print(row)
# 현재 방문하는 노드 번호를 인자로 받음
def dfs(now):
    print(now)
    for nxt in range(len(adj)):
        # now에서 nxt로 가는 간선이 있을 때만 nxt번 노드로 탐색을 진행
        if adj[now][nxt]:
            dfs(nxt)

# 0번 노드에서부터 탐색을 시작
dfs(0)