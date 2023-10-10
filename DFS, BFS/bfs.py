from collections import deque

adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][2] = 1
adj[1][3] = adj[1][4] = 1
adj[2][5] = adj[2][6] = 1
adj[3][7] = adj[3][8] = 1
adj[4][9] = 1
adj[6][10] = adj[6][11] = adj[6][12] = 1
# for row in adj:
#     print(row)
def bfs():
    dq = deque()
    # 탐색 시작할 루트 노드를 넣어줌
    dq.append(0)
    # 비어 있을 때까지 계속 반복
    while dq:
        now = dq.popleft()
        for nxt in range(len(adj)):
            # now에서 nxt로 노드가 존재한다면 deque에다가 nxt를 넣어줌
            if adj[now][nxt]:
                print(nxt)
                dq.append(nxt)
    # 더 이상 갈 수 있는 간선이 없는 leaf node를 만나면 점점 값이 줄어서 마지막에는 deque이 비게 되서 반복문 탈출하고 끝나게 됨
bfs()