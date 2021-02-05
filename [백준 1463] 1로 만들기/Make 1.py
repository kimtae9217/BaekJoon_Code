# 점화식 : f(n) = 1 + min(f(n//3), f(n//2), f(n-1))

X = int(input())
dp = [0, 0, 1, 1, 2] # 1 2 3 4 5 순서대로 연산 횟수 저장
for i in range(5, X + 1): # 5부터 X+1까지 반복
    dp.append(dp[i-1] + 1) # -1 연산 + 1회(최소 연산의 개수 계산)
    if i % 3 == 0: # 3으로 나눠진다면
        dp[i] = min(dp[i], dp[i//3]+1) # 최소 연산 비교
    if i % 2 == 0: # 2로 나눠진다면
        dp[i] = min(dp[i], dp[i//2]+1) # 최소 연산 비교
print(dp[X])


# 비슷하지만 또 다른풀이
        
# X = int(input())
# dp = [0 for _ in range(X+1)]
# for i in range(1, X+1):
#     if i == 1:
#         dp[i] == 0
#     else:
#         dp[i] = dp[i-1] + 1
#         if i % 3 == 0:
#             dp[i] = min(dp[i], dp[i//3]+1)
#         if i % 2 == 0:
#             dp[i] = min(dp[i], dp[i//2]+1)
# print(dp[i])