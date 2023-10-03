# 동전 0
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

answer = 0
for c in coins[::-1]:
    answer += k // c
    k %= c
    if k == 0:
        break
print(answer)