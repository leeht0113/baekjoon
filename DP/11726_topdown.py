# 2×n 타일링
import sys

sys.setrecursionlimit(10**7)

n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

def f(n):
    if dp[n] == 0:
        dp[n] = f(n - 2) + f(n - 1)

    return dp[n]

print(f(n) % 10007)