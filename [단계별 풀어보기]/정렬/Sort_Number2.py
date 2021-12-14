import sys

N = int(sys.stdin.readline())
N_list = []

for i in range(N):
    a = int(sys.stdin.readline())
    N_list.append(a)

N_list.sort()

for i in N_list:
    print(i)