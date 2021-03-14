N = int(input())
A = list(map(int, input().split()))

temp = [0 for _ in range(N)]

result = -1001

for i in range(N):
    temp[i] = max(temp[i-1] + A[i], A[i])
    result  = max(result, temp[i])

print(result)