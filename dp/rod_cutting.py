price = [1, 5, 8]
n = len(price)
dp = [0]*(n+1)

for i in range(1, n+1):
    for j in range(i):
        dp[i] = max(dp[i], price[j] + dp[i-j-1])

print(dp[n])
