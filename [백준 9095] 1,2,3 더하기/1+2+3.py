# 점화식 : dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
test_case = int(input())

input_n=[]
for i in range(test_case):
    input_n.append(int(input()))
dp=[1,2,4]

for i in range(3, max(input_n)):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for i in input_n:
    print(dp[i-1])
