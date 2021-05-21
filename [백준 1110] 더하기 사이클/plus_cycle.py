import sys
N = int(sys.stdin.readline())  # 입력받을 숫자 N

num = N  # 새로운 수(new_num)과 비교하기 위해 새로운 변수 num 에 입력받은 N을 지정
cnt = 0  # 사이클 카운트를 위한 변수

while True:
    sum_num = (num // 10) + (num % 10)  # N을 10으로 나눈 몫(십의 자리수) + N을 10으로 나눈 나머지(일의 자리수)
    new_num = ((num % 10)*10) + (sum_num % 10)  # 새로 만들어지는 수
    # 새로운 수의 십의 자리 => num 의 일의자리
    # 새로운 수의 일의 자리 => sum_num 의 일의자리
    cnt += 1  # 사이클 카운트 +1

    if new_num == N:  # 만약 새로운 수가 처음 입력받은 수 N 과 같다면
        break  # 멈춰!
    num = new_num  # 그렇지 않으면 num 에 마지막에 나온 새로운 수(new_num)의 값으로 재지정 후 while문 반복

print(cnt)  # 사이클 출력