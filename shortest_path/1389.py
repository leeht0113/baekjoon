# 케빈 베이컨의 6단계 법칙
INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
answer = []
for i in range(1, n  + 1):
    kevin = 0
    for j in range(1, n + 1):
        kevin += graph[i][j]
    answer.append(kevin)

for idx, a in enumerate(answer):
    if a == min(answer):
        print(idx + 1)
        break