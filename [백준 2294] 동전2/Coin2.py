n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))  
      
coin.sort()

dp = [10001 for i in  range(k+1)]
dp[0] = 0

for i in range(n) :
    for j in range(coin[i], k+1) :
        dp[j] = min(dp[j], dp[j - coin[i]] + 1)

print(dp[-1] if dp[-1] != 10001 else -1)