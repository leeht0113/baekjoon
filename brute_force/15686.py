# 치킨 배달
from itertools import combinations

n, m = map(int, input().split())
houses = []
chickens = []

for i in range(n):
    for j, value in enumerate(list(map(int, input().split()))):
        if value == 1:
            houses.append((i, j))
        elif value == 2:
            chickens.append((i, j))

answer = float('inf')
for combi in combinations(chickens, m):
    total = 0
    for house in houses:
        temp = []
        for c in combi:
            temp.append(abs(house[0] - c[0]) + abs(house[1] - c[1]))
        total += min(temp)
    answer = min(answer, total)

print(answer)