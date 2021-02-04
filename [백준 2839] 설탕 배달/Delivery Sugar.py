N = int(input()) # N kg 배달 입력
cnt = 0 # 봉지 개수

while True:
  if (N % 5) == 0 : # 5kg 로 나눠 떨어질때
    cnt += (N // 5) # 봉지 개수 세주기
    print(cnt) # 봉지 개수 출력
    break

  N -= 3 # if조건에 충족되지않을 때 N kg 에서 3kg를 빼줌
  cnt += 1 # 봉지 개수 추가 

  if (N < 0) : # 정확하게 N kg를 만들수 없다면 
    print(-1) # -1 출력
    break
  

  