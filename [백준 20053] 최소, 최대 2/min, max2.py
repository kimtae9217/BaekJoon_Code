import sys


T = int(sys.stdin.readline()) # 테스트 케이스 

for i in range(T):
    N = int(sys.stdin.readline()) # 정수의 개수 N 입력
    N_list = list(map(int, input().split())) # N개의 정수들을 공백으로 입력
    
    print('{} {}'.format(min(N_list), max(N_list)))