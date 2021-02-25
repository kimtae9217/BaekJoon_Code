A = int(input()) # 수열 A의 크기

arr = list(map(int, input().split())) # 수열 A를 이루고 있는 A[i]를 담은 배열

dp = [1 for i in range(A)] # arr[i]를 마지막 원소로 가질 때 가장 긴 증가하는 부분 수열의 길이 
                           # dp[i]의 값을 1로 초기화
for i in range(A):
    for j in range(i):
        if arr[i] > arr[j]: # 현재 위치(i)보다 이전에 있는 원소(j)가 작은지 확인
            dp[i] = max(dp[i], dp[j]+1) # 작으면 현재 위치의 이전 숫자 중, dp 최대값을 구하고 그 길이에 +1을 해줌

print(max(dp))
