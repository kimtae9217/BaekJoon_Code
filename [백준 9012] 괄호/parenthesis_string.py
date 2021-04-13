# a = int(input())
# for i in range(a):
#     b = input()
#     s = list(b)
#     sum = 0
#     for i in s:
#         if i == '(':
#             sum += 1
#         elif i == ')':
#             sum -= 1
#         if sum < 0:
#             print('NO')
#             break
#     if sum > 0:
#         print('NO')
#     elif sum == 0:
#         print('YES')

# 시간이 좀 더 빠른 풀이 방법
import sys


def solve():
    data = sys.stdin.readline().rstrip()
    stack = []
    for item in data:
        if item == '(':
            stack.append(item)
        else:
            if len(stack) == 0:
                print("NO")
                return
            else:
                stack.pop()
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")


t = int(sys.stdin.readline())  # T개의 테스트 데이터 입력
for _ in range(t):
    solve()
