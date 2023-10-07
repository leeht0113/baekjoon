# 이항 계수 2
import sys

sys.setrecursionlimit(10000)
n, k = map(int, input().split())

dp = [[-1] * (k+1) for _ in range(n+1)]

for i in range(len(dp)):
    dp[i][0] = 1
    if i <= k:
        dp[i][i] = 1

def f(n , k):

    if dp[n][k] == -1:
        dp[n][k] = f(n-1, k-1) + f(n-1, k)

    return dp[n][k]

print(f(n , k) % 10007)
