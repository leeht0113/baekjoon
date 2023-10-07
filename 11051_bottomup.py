# 이항 계수 2
n, k = map(int, input().split())

dp = [[-1] * (k+1) for _ in range(n+1)]

for i in range(len(dp)):
    dp[i][0] = 1
    if i <= k:
        dp[i][i] = 1

for i in range(2, n+1):
    for j in range(1, k+1):
        if i != j:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][k] % 10007)