# 일곱 난쟁이
from itertools import combinations
dwarf = []
for _ in range(9):
    dwarf.append(int(input()))

answer = []
for c in combinations(dwarf, 7):
    if sum(c) == 100:
        answer.append(c)

for a in sorted(answer[0]):
    print(a)