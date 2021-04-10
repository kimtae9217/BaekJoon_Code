import sys

N = int(sys.stdin.readline())


class Queue:
    def __init__(self):
        self.list = []

    def push(self, x):
        self.list.append(x)

    def pop(self):
        if self.empty():
            return -1
        else:
            output = self.list[0]
            self.list = self.list[1:]

            return output

    def empty(self):
        return 1 if len(self.list) == 0 else 0

    def size(self):
        return len(self.list)

    def front(self):
        if self.empty():
            return -1
        else:
            return self.list[0]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.list[-1]


queue = Queue()

while N > 0:
    N -= 1
    input_split = sys.stdin.readline().split()
    command = input_split[0]

    if command == 'push':
        queue.push(input_split[1])
    elif command == 'pop':
        print(queue.pop())
    elif command == 'size':
        print(queue.size())
    elif command == 'empty':
        print(queue.empty())
    elif command == 'front':
        print(queue.front())
    elif command == 'back':
        print(queue.back())
