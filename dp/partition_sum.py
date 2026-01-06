arr = [1, 5, 11, 5]
total = sum(arr)

if total % 2 != 0:
    print(False)
else:
    target = total // 2
    dp = [False]*(target+1)
    dp[0] = True

    for num in arr:
        for j in range(target, num-1, -1):
            dp[j] = dp[j] or dp[j-num]

    print(dp[target])
