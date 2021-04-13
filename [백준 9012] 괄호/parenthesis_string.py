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
            # ')' 를 입력받을 경우 이전에 '('을 입력받은 적이 없는 경우, VPS가 아님
            if not stack:  # if len(stack) == 0: 도 가능
                print("NO")
                return  # 종료
            # stack에 '('가 있으므로 꺼냄
            else:
                stack.pop()
    # 괄호를 전부 다 돌았는데 stack 안에 data가 남아 있다면 VPS가 아님
    if not stack:  # if len(stack) == 0: 도 가능
        print("YES")
    else:
        print("NO")


t = int(sys.stdin.readline())  # T개의 테스트 데이터 입력
for _ in range(t):
    solve()
