import sys

N = int(sys.stdin.readline())
stack = []

def push(x): 
    stack.append(x)

def pop():
    if(not stack):
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    return 0 if stack else 1

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

