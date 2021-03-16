n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        dp[i] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    else:
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

rem = sum(dp[n]) % 1000000000
print(rem)