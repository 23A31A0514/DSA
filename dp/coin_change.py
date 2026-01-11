coins = [1, 2, 5]
amount = 5
dp = [0] * (amount + 1)
dp[0] = 1

for c in coins:
    for i in range(c, amount + 1):
        dp[i] += dp[i - c]

print(dp[amount])
