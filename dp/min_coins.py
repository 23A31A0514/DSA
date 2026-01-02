coins = [1, 3, 4]
amount = 6
dp = [100] * (amount + 1)
dp[0] = 0

for i in range(1, amount + 1):
    for c in coins:
        if i >= c:
            dp[i] = min(dp[i], dp[i-c] + 1)

print(dp[amount])
