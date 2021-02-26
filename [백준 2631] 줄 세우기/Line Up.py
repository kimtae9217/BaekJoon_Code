n = int(input())

children = []
for i in range(n):
    children.append(int(input()))

dp = [0 for i in range(n)]
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if children[j] < children[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))