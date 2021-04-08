import sys

# N의 정수 입력
N = int(sys.stdin.readline())
# stack 리스트 초기화
stack = []


# 정수 X를 스택에 넣는 연산
def push(x):
    stack.append(x)


# 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력
# 만약 스택에 들어있는 정수가 없는 경우, -1 출력
def pop():
    if not stack:
        return -1
    else:
        return stack.pop()


# 스택에 들어있는 정수의 개수를 출력
def size():
    return len(stack)


# 스택이 비어있으면 1, 아니면 0 출력
def empty():
    return 0 if stack else 1


# 스택 가장 위에 있는 정수 출력
# 만약 스택에 들어있는 정수가 없는 경우, -1 출력
def top():
    return stack[-1] if stack else -1


for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        push(cmd[1])
    elif cmd[0] == "pop":
        print(pop())
    elif cmd[0] == "size":
        print(size())
    elif cmd[0] == "empty":
        print(empty())
    elif cmd[0] == "top":
        print(top())
