n = 5
dp = [0]*(n+1)
dp[0] = 1

for i in range(1, n+1):
    if i-1 >= 0:
        dp[i] += dp[i-1]
    if i-3 >= 0:
        dp[i] += dp[i-3]

print(dp[n])
