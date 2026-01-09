arr = [2, 3, 7]
target = 5
n = len(arr)

dp = [[False]*(target+1) for _ in range(n+1)]
dp[0][0] = True

for i in range(1, n+1):
    for j in range(target+1):
        if arr[i-1] <= j:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][target])
